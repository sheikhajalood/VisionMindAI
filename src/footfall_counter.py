
from pathlib import Path

import cv2
from ultralytics import YOLO


# ==========================================
# VISIONMIND AI - FOOTFALL COUNTER
# ==========================================

PROJECT_DIR = Path(__file__).resolve().parent.parent
VIDEO_FILE = PROJECT_DIR / "footfall_test.mp4"
MODEL_FILE = PROJECT_DIR / "yolo11n.pt"
OUTPUT_DIR = PROJECT_DIR / "data" / "processed"

CONFIDENCE = 0.20
IMAGE_SIZE = 640
LINE_POSITION_RATIO = 0.50
MAX_MISSING_FRAMES = 15


def main():
    # 1. Check required files
    if not VIDEO_FILE.exists():
        raise FileNotFoundError(f"Video not found: {VIDEO_FILE}")

    if not MODEL_FILE.exists():
        raise FileNotFoundError(f"YOLO model not found: {MODEL_FILE}")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # 2. Load YOLO
    print("Loading YOLO model...", flush=True)
    model = YOLO(str(MODEL_FILE))

    # 3. Read video properties
    capture = cv2.VideoCapture(str(VIDEO_FILE))

    if not capture.isOpened():
        raise RuntimeError(f"Could not open video: {VIDEO_FILE}")

    fps = capture.get(cv2.CAP_PROP_FPS)
    width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total_frames = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
    capture.release()

    if width <= 0 or height <= 0:
        raise RuntimeError("Could not read the video's dimensions.")

    if fps <= 0:
        fps = 25.0

    line_y = int(height * LINE_POSITION_RATIO)

    print(f"Video: {VIDEO_FILE.name}")
    print(f"Resolution: {width} x {height}")
    print(f"Frames in video: {total_frames}")
    print("Starting person detection and tracking...", flush=True)

    # 4. Create output video
    output_video = OUTPUT_DIR / "footfall_demo.avi"

    writer = cv2.VideoWriter(
        str(output_video),
        cv2.VideoWriter_fourcc(*"XVID"),
        fps,
        (width, height),
    )

    if not writer.isOpened():
        raise RuntimeError(
            "Could not create output video. Check OpenCV codec support."
        )

    # 5. Initialise counting information
    previous_positions = {}
    last_seen_frames = {}
    counted_ids = set()

    frames_processed = 0
    total_person_detections = 0

    try:
        # 6. Track people in the video
        results = model.track(
            source=str(VIDEO_FILE),
            tracker="bytetrack.yaml",
            classes=[0],
            conf=CONFIDENCE,
            imgsz=IMAGE_SIZE,
            persist=True,
            stream=True,
            verbose=False,
        )

        for result in results:
            frame = result.orig_img.copy()
            frames_processed += 1

            # Print progress every 25 frames
            if frames_processed % 25 == 0:
                print(
                    f"Processing frame {frames_processed}"
                    f" / {total_frames}...",
                    flush=True,
                )

            # Draw the counting line
            cv2.line(
                frame,
                (0, line_y),
                (width, line_y),
                (0, 255, 255),
                2,
            )

            cv2.putText(
                frame,
                "COUNTING LINE",
                (10, max(line_y - 10, 25)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 255),
                2,
            )

            # 7. Read person detections and tracking IDs
            if result.boxes is not None and result.boxes.id is not None:
                boxes = result.boxes.xyxy.cpu().tolist()
                track_ids = result.boxes.id.int().cpu().tolist()

                total_person_detections += len(track_ids)

                for box, track_id in zip(boxes, track_ids):
                    x1, y1, x2, y2 = map(int, box)

                    # Bottom-centre point of the person box
                    foot_x = (x1 + x2) // 2
                    foot_y = y2

                    # Draw bounding box, ID and anchor point
                    cv2.rectangle(
                        frame,
                        (x1, y1),
                        (x2, y2),
                        (255, 0, 0),
                        2,
                    )

                    cv2.circle(
                        frame,
                        (foot_x, foot_y),
                        5,
                        (0, 0, 255),
                        -1,
                    )

                    cv2.putText(
                        frame,
                        f"ID {track_id}",
                        (x1, max(y1 - 8, 20)),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.5,
                        (255, 0, 0),
                        2,
                    )

                    previous_y = previous_positions.get(track_id)

                    # Count the first crossing for this track ID.
                    # Both upward and downward movement count.
                    if (
                        previous_y is not None
                        and track_id not in counted_ids
                    ):
                        crossed_down = (
                            previous_y < line_y <= foot_y
                        )
                        crossed_up = (
                            previous_y > line_y >= foot_y
                        )

                        if crossed_down or crossed_up:
                            counted_ids.add(track_id)

                    # Save the current position and last-seen frame
                    previous_positions[track_id] = foot_y
                    last_seen_frames[track_id] = frames_processed

            # 8. Remove stale tracking history
            expired_ids = [
                track_id
                for track_id, last_seen in last_seen_frames.items()
                if frames_processed - last_seen > MAX_MISSING_FRAMES
            ]

            for track_id in expired_ids:
                last_seen_frames.pop(track_id, None)
                previous_positions.pop(track_id, None)

            # 9. Add statistics to the output video
            cv2.rectangle(
                frame,
                (5, 5),
                (350, 75),
                (0, 0, 0),
                -1,
            )

            cv2.putText(
                frame,
                f"Crossings: {len(counted_ids)}",
                (15, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2,
            )

            cv2.putText(
                frame,
                f"Frame: {frames_processed}/{total_frames}",
                (15, 58),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (255, 255, 255),
                2,
            )

            writer.write(frame)

    finally:
        writer.release()

    # 10. Print final report
    print("\n======================================")
    print(" VISIONMIND AI - FOOTFALL REPORT")
    print("======================================")
    print(f"Frames processed: {frames_processed}")
    print(f"Person detections across frames: {total_person_detections}")
    print(f"Tracked IDs counted crossing: {len(counted_ids)}")
    print(f"Annotated video: {output_video}")
    print("--------------------------------------")
    print("Counting rule: First crossing per track ID")
    print("Direction: Both upward and downward")
    print("Warning: Track IDs are not guaranteed to represent unique people.")
    print("Compare the result with manually observed crossings.")
    print("======================================")


if __name__ == "__main__":
    main()

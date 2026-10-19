
from pathlib import Path
from ultralytics import YOLO

# Project paths
PROJECT_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = PROJECT_DIR / "data" / "processed"

# Load the pretrained YOLO model
model = YOLO("yolo11n.pt")

# Track people moving through the video
results = model.track(
    source="solutions_ci_demo.mp4",
    tracker="bytetrack.yaml",
    classes=[0],          # Person class only
    conf=0.20,
    persist=True,
    save=True,
    project=str(OUTPUT_DIR),
    name="person_tracking",
    exist_ok=True,
    stream=True,
    verbose=False
)

frames_processed = 0
frames_with_tracks = 0
unique_track_ids = set()

for result in results:
    frames_processed += 1

    if result.boxes.id is not None:
        frames_with_tracks += 1

        track_ids = result.boxes.id.int().cpu().tolist()
        unique_track_ids.update(track_ids)

print("\n===== VISIONMIND AI TRACKING REPORT =====")
print(f"Frames processed: {frames_processed}")
print(f"Frames with tracked people: {frames_with_tracks}")
print(f"Different track IDs observed: {len(unique_track_ids)}")
print("Note: track IDs are not guaranteed to represent unique people.")
print(f"Annotated video folder: {OUTPUT_DIR / 'person_tracking'}")

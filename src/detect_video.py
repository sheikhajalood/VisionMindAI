
from pathlib import Path
from ultralytics import YOLO

PROJECT_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = PROJECT_DIR / "data" / "processed"

model = YOLO("yolo11n.pt")

results = model.predict(
    source="solutions_ci_demo.mp4",
    classes=[0],              # Person class only
    conf=0.20,                 # Lower confidence threshold
    save=True,
    project=str(OUTPUT_DIR),
    name="person_detection_test",
    exist_ok=True,
    stream=True,
    verbose=False
)

frames_processed = 0
person_detections = 0

for result in results:
    frames_processed += 1
    person_detections += len(result.boxes)

print("\n===== PERSON DETECTION TEST =====")
print(f"Frames processed: {frames_processed}")
print(f"Person detections across frames: {person_detections}")
print("These are detections, not unique people.")
print(f"Output folder: {OUTPUT_DIR / 'person_detection_test'}")


from pathlib import Path
from ultralytics import YOLO

# Locate the main project folder
PROJECT_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = PROJECT_DIR / "data" / "processed"

# Load a small pretrained YOLO model
model = YOLO("yolo11n.pt")

# Detect objects in a sample image
results = model.predict(
    source="https://ultralytics.com/images/bus.jpg",
    save=True,
    project=str(OUTPUT_DIR),
    name="yolo_demo",
    exist_ok=True
)

# Print detected object names and confidence scores
for result in results:
    print("\n===== VISIONMIND AI: OBJECT DETECTION =====")

    for box in result.boxes:
        class_id = int(box.cls[0])
        confidence = float(box.conf[0])
        label = model.names[class_id]

        print(f"{label}: {confidence:.2%} confidence")

print("\nDetection complete!")
print(f"Results folder: {OUTPUT_DIR / 'yolo_demo'}")

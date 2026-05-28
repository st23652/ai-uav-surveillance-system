from ultralytics import YOLO

# Load YOLOv8 object detection model
model = YOLO("yolov8n.pt")


def detect_objects(frame):
    """
    Run AI object detection on input frame.
    """

    # Perform inference
    results = model(frame)

    return results

from ultralytics import YOLO

# Load an official or custom model
# model = YOLO('yolov8n.pt')  # Load an official Detect model
model = YOLO('fishtracking/best.pt')  # Load an official Detect model
# model = YOLO('yolov8n-seg.pt')  # Load an official Segment model
# model = YOLO('yolov8n-pose.pt')  # Load an official Pose model
# model = YOLO('path/to/best.pt')  # Load a custom trained model

# Perform tracking with the model
# results = model.track(source="https://youtu.be/Zgi9g1ksQHc", show=True)  # Tracking with default tracker
# results = model.track(source="https://youtu.be/Zgi9g1ksQHc", show=True, tracker="bytetrack.yaml")  # Tracking with ByteTrack tracker
# results = model.track(source="/home/q_hu/workspace6/MOT/ultralytics/videos/10-fish-part2-2016_raw.mp4", show=False, tracker="bytetrack.yaml", save_txt=True, save=True, save_conf=True)  # Tracking with ByteTrack tracker
results = model.track(source="fishtracking/video/sample.mp4", show=False, tracker="bytetrack.yaml", save_txt=True, save=True, save_conf=True)  # Tracking with ByteTrack tracker
# print(results)

from ultralytics import YOLO

# Load Pretrained Model
model = YOLO("yolov8n.pt") 

# Train Model
model.train(data="../data/train.yaml", epoch="50", patience="5", batch="16") 
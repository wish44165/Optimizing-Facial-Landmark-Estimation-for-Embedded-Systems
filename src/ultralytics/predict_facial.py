from ultralytics import YOLO

# Load a model
model = YOLO('./runs/facial/train/weights/best.pt')  # load a custom model

# Predict with the model
results = model('./data/images/val/', save=True, project="./runs/facial")
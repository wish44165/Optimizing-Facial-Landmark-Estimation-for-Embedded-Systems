from ultralytics import YOLO

# Load a model
model = YOLO('./runs/facial/train5/weights/best.pt')  # load a custom model

# Predict with the model
results = model('../preprocess/data_v2/images/val/', save=True, save_txt=True, project="./runs/facial")
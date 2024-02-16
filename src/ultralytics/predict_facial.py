from ultralytics import YOLO

# Load a model
model = YOLO('./runs/facial/train/weights/best.pt')  # load a custom model

# Predict with the model
results = model('../../ivslab_facial_train/ibug/images/', save=True, project="./runs/facial")
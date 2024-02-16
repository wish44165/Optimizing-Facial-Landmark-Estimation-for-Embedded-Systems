import os
from ultralytics import YOLO

os.environ["OMP_NUM_THREADS"]='8'
os.environ["KMP_DUPLICATE_LIB_OK"]='TRUE'

# Load a model
model = YOLO('yolov8n-pose.pt')  # load a pretrained model (recommended for training)

if __name__ == '__main__':
    # Train the model
    model.train(data='./facial.yaml', epochs=100, batch=8, imgsz=640, device=0, workers=8, project='./runs/facial')
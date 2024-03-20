from ultralytics import YOLO

# Load a model
model = YOLO('./best.pt')  # load a pretrained model (recommended for training)

# Use the model
path = model.export(imgsz=640, half=False, int8=True, format="tflite")  # export the model to ONNX format
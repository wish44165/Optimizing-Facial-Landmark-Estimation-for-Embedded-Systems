import argparse
from ultralytics import YOLO

def parse_opt(known=False):
    parser = argparse.ArgumentParser()
    parser.add_argument('--weight', type=str, default='./best.tflite', help='trained model')
    parser.add_argument('--save_path', type=str, default='./runs/facial', help='Save path')
    parser.add_argument('--predict_folder', type=str, default='/home/wish/pro/ICME2024/datasets/ivslab_facial_test_private_qualification', help='Predict folder')
    parser.add_argument('--imgsz', type=int, default=96, help='Image size')
    parser.add_argument('--conf', type=float, default=0.5, help='')
    return parser.parse_known_args()[0] if known else parser.parse_args()

opt = parse_opt()

# Load a model
tflite_model = YOLO(opt.weight, task='pose')  # load a custom model

# Predict with the model
results = tflite_model(opt.predict_folder, save=True, save_txt=True, project=opt.save_path, imgsz=opt.imgsz, conf=opt.conf)
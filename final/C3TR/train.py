import os
import argparse
from ultralytics import YOLO

os.environ['CUDA_LAUNCH_BLOCKING'] = '1'
#os.environ["OMP_NUM_THREADS"]='8'
#os.environ["KMP_DUPLICATE_LIB_OK"]='TRUE'

def parse_opt(known=False):
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_name', type=str, default='./best_v4.pt', help='model name')
    parser.add_argument('--yaml_path', type=str, default='./facial_f3.yaml', help='The yaml path')
    parser.add_argument('--n_epoch', type=int, default=300, help='Total number of training epochs.')
    parser.add_argument('--n_patience', type=int, default=100, help='Number of epochs to wait without improvement in validation metrics before early stopping the training.')
    parser.add_argument('--bs', type=int, default=128, help='Batch size')
    parser.add_argument('--imgsz', type=int, default=96, help='Image size')

    parser.add_argument('--single_cls', type=bool, default=True, help='single class or not')
    parser.add_argument('--pose', type=float, default=12.0, help='Weight of the pose loss in models trained for pose estimation, influencing the emphasis on accurately predicting pose keypoints.')
    parser.add_argument('--degrees', type=float, default=10, help='')
    parser.add_argument('--shear', type=float, default=0.2, help='')
    parser.add_argument('--mosaic', type=float, default=0.0, help='')
    parser.add_argument('--mixup', type=float, default=0.2, help='')
    parser.add_argument('--copy_paste', type=float, default=0.2, help='')
    parser.add_argument('--erasing', type=float, default=0.0, help='')


    parser.add_argument('--n_worker', type=int, default=8, help='Number of workers')
    parser.add_argument('--save_path', type=str, default='./runs/facial', help='Save path')
    return parser.parse_known_args()[0] if known else parser.parse_args()

opt = parse_opt()

# Load a model
#model = YOLO(opt.model_name)  # load a pretrained model (recommended for training)
model = YOLO('./ultralytics/cfg/models/v8/yolov8-pose.yaml').load(opt.model_name)

if __name__ == '__main__':
    # Train the model
    model.train(data=opt.yaml_path, epochs=opt.n_epoch, patience=opt.n_patience, batch=opt.bs, imgsz=opt.imgsz, device=0, workers=opt.n_worker, 
                project=opt.save_path, single_cls=opt.single_cls, pose=opt.pose, degrees=opt.degrees, shear=opt.shear, mosaic=opt.mosaic,
                mixup=opt.mixup, copy_paste=opt.copy_paste, erasing=opt.erasing)
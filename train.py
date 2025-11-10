import warnings, os

warnings.filterwarnings('ignore')
from ultralytics import RTDETR


if __name__ == '__main__':
    model = RTDETR('/home/ssj/ccx/RTDETR-20250622/RTDETR-main/ultralytics/cfg/models/rt-detr/rtdetr-WetBird.yaml')
    #model.load('/home/ssj/ccx/RTDETR-20250622/RTDETR-main/weights/rtdetr-r18.pt') # loading pretrain weights
    model.train(data='/home/ssj/ccx/RTDETR-20250622/RTDETR-main/dataset/data.yaml',
                cache=False,
                imgsz=640,
                epochs=200,
                batch=4, 
                workers=4, 
                # device='0,1', 
                #resume='', 
                project='runs/train',
                name='exp',
                )
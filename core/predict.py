import cv2
from datetime import datetime

def predict(dataset, model, ext):
    global img_y
    path = dataset[0]
    file_name = dataset[1]
    tupian_path =  model.detect(path)
    image_info = 1
    # if not cv2.imwrite('./tmp/draw/{}.{}'.format(file_name, ext), x):
    #     raise Exception('保存检测图片错了')
    return image_info
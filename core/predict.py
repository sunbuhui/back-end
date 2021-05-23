import cv2
from datetime import datetime

def predict(dataset, model, ext):
    global img_y
    x = dataset[0].replace('\\', '/')
    file_name = dataset[1]
    x = cv2.imread(x)
    img_y, image_info = model.detect(x)
    if not cv2.imwrite('./tmp/draw/{}.{}'.format(file_name, ext), x):
        raise Exception('保存检测图片错了')
    return image_info
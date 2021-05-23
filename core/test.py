import cv2
import os

if __name__ == '__main__':
    if os.path.exists('/DOTA_yolov5/proj/back-end/uploads/WechatIMG4438.jpg'):
        print('zhen1')
    if os.path.exists('/DOTA_yolov5/proj/back-end/tmp/ct/WechatIMG4438.jpg'):
        print('zhen2')
    img = cv2.imread('/DOTA_yolov5/proj/back-end/uploads/WechatIMG4438.jpg')
    # cv2.imshow('dd', img)
    if os.path.exists('./tmp/draw/{}.{}'.format('a', 'jpg')):
        print('1')
    if os.path.exists('/tmp/draw'):
        print('2')

    if not cv2.imwrite('/tmp/draw/{}.{}'.format('a', 'jpg'), img):
        print('失败了')

#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
@project: AutoXue
@file: secureRandom.py
@author: wongsyrone
@Copyright © 2019. All rights reserved.
'''
import cv2
import numpy as np

def mathc_img(image,Target,value):
    img_rgb = cv2.imread(image)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(Target,0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = value
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (7,249,151), 2)   
    cv2.imshow('Detected',img_rgb)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    image=("aa.png")
    Target=('data/subscribe.png')
    value=0.9
    mathc_img(image,Target,value)

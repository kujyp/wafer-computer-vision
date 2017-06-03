#-*- coding: utf-8 -*-

import cv2
import os


def load_allpath(path):
    res = []

    for root, dirs, files in os.walk(path):
        for file in files:
            if file[0] is '.':
                continue
            filepath = os.path.join(root, file)
            res.append(filepath)
    return res

def load_pics(dir):
    paths = load_allpath(dir)
    imgs = []

    for path in paths:
        imgs.append(cv2.imread(path))

    return imgs
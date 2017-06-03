import os

import cv2
import random

from src_0602.Logger import logger
from src_0602.Singleton import Singleton


class VideoLoader(Singleton):
    NUM_SKIP_FRAMES = 10

    def __init__(self) -> None:
        super().__init__()
        self.load()

    @property
    def getDir(self):
        return "data/mpg인코딩"

    @property
    def getFilename(self):
        filenames = []
        for root, dirs, files in os.walk(self.getDir):
            filenames += files
        nidx = len(filenames)
        rndidx = random.randint(0,nidx-1)
        filename = filenames[rndidx]
        logger.info("nidx={}, rndidx={}, filename={}".format(nidx, rndidx,filename))
        return filename

    @property
    def getFilepath(self):
        return os.path.join(self.getDir, self.getFilename)

    def load(self):
        self.video_capture = cv2.VideoCapture(self.getFilepath)

    def next(self):
        img = None
        for i in range(self.NUM_SKIP_FRAMES):
            _, img = self.video_capture.read()
            if img is None:
                break

        return img
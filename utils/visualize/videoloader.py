import cv2
import os
import random

from utils.logging_ import logger
from utils.base.singleton import Singleton


class VideoLoader(Singleton):
    NUM_SKIP_FRAMES = 30

    def __init__(self) -> None:
        super().__init__()
        self.load()

    @property
    def getDir(self):
        return "data/mpg인코딩"

    def getFilename(self, filenum=None):
        filenames = []
        for root, dirs, files in os.walk(self.getDir):
            filenames += files
        nidx = len(filenames)

        if filenum is None:
            rndidx = random.randint(0,nidx-1)
        else:
            rndidx = filenum
        filename = filenames[rndidx]
        logger.info("nidx={}, rndidx={}, filename={}".format(nidx, rndidx,filename))
        return filename

    def getFilepath(self, filenum=None):
        return os.path.join(self.getDir, self.getFilename(filenum))

    def load(self, filenum=None):
        self.video_capture = cv2.VideoCapture(self.getFilepath(filenum))

    def next(self):
        img = None
        for i in range(self.NUM_SKIP_FRAMES):
            _, img = self.video_capture.read()
            if img is None:
                break

        return img
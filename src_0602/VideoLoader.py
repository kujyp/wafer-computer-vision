import os

import cv2

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
        filename = 'ch01 Lup ch1.mpg'
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
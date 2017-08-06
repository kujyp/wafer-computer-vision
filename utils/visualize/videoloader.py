import cv2
import os
import random

from config.config import Source
from utils.base.singleton import Singleton
from utils.log.logging_ import logger


class VideoLoader(Singleton):
    def __init__(self) -> None:
        super().__init__()
        self.load()

    @property
    def get_dir(self):
        return Source.VIDEO_SOURCE_DIRECTORY

    def get_randomfilename(self):
        filenames = []

        for root, dirs, files in os.walk(self.get_dir):
            filenames += files

        nidx = len(filenames)

        rndidx = random.randint(0,nidx-1)

        filename = filenames[rndidx]
        logger.info("nidx={}, rndidx={}, filename={}".format(nidx, rndidx,filename))
        return filename

    def get_filename(self):
        filename = Source.VIDEO_SOURCE_FILENAME
        if not len(filename) > 0:
            filename = self.get_randomfilename()

        return filename

    def get_filepath(self):
        return os.path.join(self.get_dir, self.get_filename())

    def load(self):
        self.video_capture = cv2.VideoCapture(self.get_filepath())

    def next(self):
        for i in range(Source.VIDEO_NUM_SKIP_FRAMES + 1):
            _, img = self.video_capture.read()
            if img is None:
                break

        return img
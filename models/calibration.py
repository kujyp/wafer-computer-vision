import cv2
import os.path

from config.config import Source
from utils.base.singleton import Singleton


class Calibration(Singleton):
    def __init__(self) -> None:
        super().__init__()

        self.cropped_template = None
        self.load()

    def load(self):
        path = Source.CALIBRATION_CROPPED_TEMPLATE_PATH
        if os.path.isfile(path):
            self.cropped_template = cv2.imread(path)

    def isLoaded(self):
        return (self.cropped_template is not None)
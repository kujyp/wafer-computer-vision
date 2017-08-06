import cv2
import os.path

from config.config import Source
from utils.base.singleton import Singleton


class Calibration(Singleton):
    def __init__(self) -> None:
        super().__init__()

        self.CROPPED_TEMPLATE = None
        self.CROPPED_TEMPLATEPOSITION_INPIXEL = None
        self.load()

    def load(self):
        path = Source.CALIBRATION_CROPPED_TEMPLATE_PATH
        if os.path.isfile(path):
            self.CROPPED_TEMPLATE = cv2.imread(path)

        position_path = Source.CALIBRATION_CROPPED_TEMPLATEPOSITION_INPIXEL_PATH
        if os.path.isfile(position_path):
            with open(position_path) as f:
                import numpy as np
                self.CROPPED_TEMPLATEPOSITION_INPIXEL = np.load(position_path).item()

    def isLoaded(self):
        return not ((self.CROPPED_TEMPLATE is None) | (self.CROPPED_TEMPLATEPOSITION_INPIXEL is None))
import cv2
import os.path

import numpy as np

from config.config import Source
from config.consts import InNumpyarray
from utils.base.singleton import Singleton
from utils.log.logging_ import logger


class Calibration(Singleton):
    def __init__(self) -> None:
        super().__init__()

        self.CROPPED_TEMPLATE = None
        self.CROPPED_TEMPLATEPOSITION_INPIXEL = None
        self.load()

    def load(self):
        self.load_cropped_template()
        self.load_cropped_template_position()

    def is_loaded(self):
        return not ((self.CROPPED_TEMPLATE is None) | (self.CROPPED_TEMPLATEPOSITION_INPIXEL is None))

    def calibrate_with_cropped_template(self):
        logger.info('Calibrate with cropped templatefile {}.'.format(
            Source.CALIBRATION_CROPPED_TEMPLATE_FILENAME))

        template_path = Source.CALIBRATION_TEMPLATE_PATH
        if os.path.isfile(template_path):
            template = cv2.imread(template_path)
            cropped_shape = np.shape(self.CROPPED_TEMPLATE)
            from logics.region.template_register import finddelta_withtemplate
            BOUNDARYLINE_LEFT = finddelta_withtemplate(template, self.CROPPED_TEMPLATE)
            BOUNDARYLINE_RIGHT = BOUNDARYLINE_LEFT + cropped_shape[InNumpyarray.X]
            position_path = Source.CALIBRATION_CROPPED_TEMPLATEPOSITION_INPIXEL_PATH
            np.save(position_path, {Source.XSTART: BOUNDARYLINE_LEFT, Source.XEND:BOUNDARYLINE_RIGHT})

            self.load_cropped_template_position()
        else:
            raise AssertionError("TEMPLATE_FILE = {} is needed.".format(template_path))


    def load_cropped_template(self):
        cropped_path = Source.CALIBRATION_CROPPED_TEMPLATE_PATH
        if os.path.isfile(cropped_path):
            self.CROPPED_TEMPLATE = cv2.imread(cropped_path)
        else:
            AssertionError("TEMPLATE_CROPPED_FILE = {} is needed.".format(cropped_path))

    def load_cropped_template_position(self):
        position_path = Source.CALIBRATION_CROPPED_TEMPLATEPOSITION_INPIXEL_PATH
        if os.path.isfile(position_path):
            with open(position_path) as f:
                self.CROPPED_TEMPLATEPOSITION_INPIXEL = np.load(position_path).item()
        else:
            self.calibrate_with_cropped_template()
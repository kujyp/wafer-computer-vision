import numpy as np

from config.config import Source
from logics.region.template_register import finddelta_withtemplate
from logics.region.region_processor import findregion_withvertices, cropregion_withxy
from models.calibration import Calibration


def detect_target_region(image):
    imshape = image.shape

    cropped = Calibration.getInstance().CROPPED_TEMPLATE
    deltax = finddelta_withtemplate(image, cropped)

    TEMPLATE_POSITION = Calibration.getInstance().CROPPED_TEMPLATEPOSITION_INPIXEL
    XSIZEOFTEMPLATE = TEMPLATE_POSITION[Source.XEND] - TEMPLATE_POSITION[Source.XSTART]

    xst, xed = deltax, deltax + XSIZEOFTEMPLATE
    yst, yed = 0, imshape[0]
    vertices = np.array([[(xst - 50, yst), (xst - 50, yed), (xed + 50, yed), (xed + 50, yst)]], dtype=np.int32)
    masked = findregion_withvertices(image, vertices)
    position = (xst, yst, xed, yed)
    croped = cropregion_withxy(image, (xst, yst, xed, yed))

    return masked, croped, position
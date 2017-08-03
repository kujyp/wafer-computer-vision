import numpy as np

from logics.region.region_processor import findregion_withvertices, cropregion_withxy
from logics.regist.TemplateRegister import finddelta_withtemplate
from models.calibration import Calibration


def detect_target_region(image):
    imshape = image.shape

    cropped = Calibration.getInstance().cropped_template
    deltax = finddelta_withtemplate(image, cropped)
    xst, xed = deltax, deltax + (1130 - 845)
    # xst, xed = 845, 1130 # Video4
    yst, yed = 0, imshape[0]
    vertices = np.array([[(xst - 50, yst), (xst - 50, yed), (xed + 50, yed), (xed + 50, yst)]], dtype=np.int32)
    masked = findregion_withvertices(image, vertices)
    croped = cropregion_withxy(image, (xst, yst, xed, yed))

    return masked, croped
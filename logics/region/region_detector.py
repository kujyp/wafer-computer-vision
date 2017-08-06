import numpy as np

from config.config import Source
from logics.region.region_processor import findregion_withvertices, cropregion_withxy
from logics.region.template_register import regist
from utils.calibration.calibration import Calibration


def detect_target_region(image):
    """
    타겟의 지점을 Segmentation
    
    :param image: 원본이미지 
    :return: 찾아낸 타겟을 자른 Mask 이미지, Mask이미지를 잘린부분만 떼어넨 Resize이미지, 타겟의 위치 Position = (xst, yst, xed, yed)
    """
    imshape = image.shape

    cropped = Calibration.getInstance().CROPPED_TEMPLATE
    deltax = regist(image, cropped)

    TEMPLATE_POSITION = Calibration.getInstance().CROPPED_TEMPLATEPOSITION_INPIXEL
    XSIZEOFTEMPLATE = TEMPLATE_POSITION[Source.XEND] - TEMPLATE_POSITION[Source.XSTART]

    xst, xed = deltax, deltax + XSIZEOFTEMPLATE
    yst, yed = 0, imshape[0]
    vertices = np.array([[(xst - 50, yst), (xst - 50, yed), (xed + 50, yed), (xed + 50, yst)]], dtype=np.int32)
    masked = findregion_withvertices(image, vertices)
    position = (xst, yst, xed, yed)
    croped = cropregion_withxy(image, position)

    return masked, croped, position
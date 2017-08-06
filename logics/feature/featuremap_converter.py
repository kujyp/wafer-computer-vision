from config.consts import FeatureMethod
from logics.feature.corner_detector import detect_corner_with_fast
from logics.feature.gradient_detector import gradient_y, canny, gradient_x, gradient


def convert_feature_map(image, method=FeatureMethod.Canny):
    """
    원본이미지에서 Feature 추출
    
    :param image: 원본 이미지
    :param method: 적용할 Method
    :return: mask: Feature Only 이미지, overwrite: Feature + Original 이미지
    """
    mask, overwrite = None, None
    if method == FeatureMethod.Fast:
        mask, overwrite = detect_corner_with_fast(image)
    elif method == FeatureMethod.Canny:
        mask = canny(image)
    elif method == FeatureMethod.GradientX:
        mask = gradient_x(image)
    elif method == FeatureMethod.GradientY:
        mask = gradient_y(image)
    elif method == FeatureMethod.Gradient:
        mask = gradient(image)

    return mask, overwrite
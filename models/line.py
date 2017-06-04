import cv2

from utils.logging_ import logger


class Line():
    @classmethod
    def drawLines(cls, image, lines, color=(0, 0, 255)):
        img = image[:]
        for line in lines:
            x1, y1, x2, y2 = line[0]
            logger.debug("drawLines x1,y1,x2,y2={},{},{},{}".format(x1, y1, x2, y2))
            cv2.line(img, (x1, y1), (x2, y2), color, 2)

        return img
import cv2

from config.config import Window
from utils.base.singleton import Singleton
from utils.log.logging_ import logger


class WindowManager(Singleton):
    def __init__(self) -> None:
        super().__init__()
        self.windowNames = []
        self.width = int(Window.FULL_SCREEN_WIDTH / Window.NUMOF_WINDOW_COLUMNS)
        self.height = int(Window.FULL_SCREEN_HEIGHT / Window.NUMOF_WINDOW_ROWS)
        self.other_height = self.height + Window.FIXED_BAR_HEIGHT
        self.windowNames = Window.WINDOWNAMES

    def showWindows(self):
        for idx, name in enumerate(self.windowNames):
            cv2.namedWindow(name, cv2.WINDOW_KEEPRATIO)
            cv2.resizeWindow(name, self.width, self.height)
            colnum = int(idx % Window.NUMOF_WINDOW_COLUMNS)
            rownum = int(idx / Window.NUMOF_WINDOW_COLUMNS)
            cv2.moveWindow(name, self.width * colnum, self.other_height * rownum)


    def imgshow(self,img, window_position_or_name):
        if img is None:
            logger.error("image is None")
            return
            # raise ValueError("image is None")
        img = cv2.resize(img, (self.width, self.height))
        if type(window_position_or_name) is int:
            # logger.debug("windowName is int")
            idx = window_position_or_name
            cv2.imshow(self.windowNames[idx], img)
        else:
            # logger.debug("windowName is not int")
            if window_position_or_name in self.windowNames: # check windowName is in Names
                cv2.imshow(window_position_or_name, img)
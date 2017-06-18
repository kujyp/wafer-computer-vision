import cv2

from utils.base.singleton import Singleton
from utils.logging_ import logger

# FULL_SCREEN_WIDTH = 1000
# FULL_SCREEN_HEIGHT = 950
FULL_SCREEN_WIDTH = 959*2
FULL_SCREEN_HEIGHT = 1000
FIXED_BAR_HEIGHT = 40
NUMOFCOLS = 4

class WindowManager(Singleton):
    def __init__(self) -> None:
        super().__init__()
        self.windowNames = []

    @property
    def numofWindows(self):
        return len(self.windowNames)

    def addWindow(self, windowNames):
        if isinstance(windowNames, list):
            iterator = windowNames
        else:
            iterator = [windowNames]

        for name in iterator:
            self.addWindowName(name)

        self.showWindows()

    # def showWindows(self):
    #     self.width = int(FULL_SCREEN_WIDTH / self.numofWindows)
    #     self.height = int(FULL_SCREEN_HEIGHT)
    #     for idx, name in enumerate(self.windowNames):
    #         cv2.namedWindow(name, cv2.WINDOW_KEEPRATIO)
    #         cv2.resizeWindow(name, self.width, self.height)
    #         cv2.moveWindow(name, self.width * idx, 0)

    def showWindows(self):
        numofCols = NUMOFCOLS
        numofRows = self.numofWindows / numofCols
        self.width = int(FULL_SCREEN_WIDTH / numofCols)
        self.height = int(FULL_SCREEN_HEIGHT / numofRows)
        other_height = self.height + FIXED_BAR_HEIGHT
        for idx, name in enumerate(self.windowNames):
            cv2.namedWindow(name, cv2.WINDOW_KEEPRATIO)
            cv2.resizeWindow(name, self.width, self.height)
            colnum = int(idx % numofCols)
            rownum = int(idx / numofCols)
            cv2.moveWindow(name, self.width * colnum, other_height * rownum)


    def addWindowName(self, name):
        self.windowNames.append(name)

    def imgshow(self,img, windowName):
        if img is None:
            logger.error("image is None")
            return
            # raise ValueError("image is None")
        img = cv2.resize(img, (self.width, self.height))
        if type(windowName) is int:
            # logger.debug("windowName is int")
            idx = windowName
            cv2.imshow(self.windowNames[idx], img)
        else:
            # logger.debug("windowName is not int")
            if windowName in self.windowNames: # check windowName is in Names
                cv2.imshow(windowName,img)
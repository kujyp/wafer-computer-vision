import cv2

from utils.base.singleton import Singleton

FULL_SCREEN_WIDTH = 959*2
FULL_SCREEN_HEIGHT = 1000

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

    def showWindows(self):
        self.width = int(FULL_SCREEN_WIDTH / self.numofWindows)
        self.height = int(FULL_SCREEN_HEIGHT)
        for idx, name in enumerate(self.windowNames):
            cv2.namedWindow(name, cv2.WINDOW_KEEPRATIO)
            cv2.resizeWindow(name, self.width, self.height)
            cv2.moveWindow(name, self.width * idx, 0)


    def addWindowName(self, name):
        self.windowNames.append(name)

    def imgshow(self,img, windowName):
        img = cv2.resize(img, (self.width, self.height))
        if windowName in windowName: # check windowName is in Names
            cv2.imshow(windowName,img)
import cv2
import types

from src_0602.Singleton import Singleton


class WindowManager(Singleton):
    def __init__(self) -> None:
        super().__init__()
        self.numofWindows = 0
        self.width = 959
        self.height = 1000
        self.windowName = []

    def addWindow(self, windowNames):
        if isinstance(windowNames, list):
            iterator = windowNames
        else:
            iterator = [windowNames]

        for name in iterator:
            cv2.namedWindow(name, cv2.WINDOW_KEEPRATIO)
            cv2.resizeWindow(name, self.width, self.height)
            cv2.moveWindow(name, self.width*self.numofWindows,0)
            self.addWindowName(name)
            self.numofWindows += 1

    def addWindowName(self, name):
        self.windowName.append(name)

    def imgshow(self,img, windowName):
        img = cv2.resize(img, (self.width, self.height))
        if windowName in windowName: # check windowName is in Names
            cv2.imshow(windowName,img)
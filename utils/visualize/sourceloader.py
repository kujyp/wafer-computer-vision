from config.config import Source
from config.consts import MediaTypes
from utils.base.singleton import Singleton
from utils.visualize.videoloader import VideoLoader


class SourceLoader(Singleton):
    def __init__(self) -> None:
        super().__init__()
        self.source = None
        if Source.INPUT_MEDIA_TYPE == MediaTypes.VIDEO:
            self.source = VideoLoader.getInstance()
        elif Source.INPUT_MEDIA_TYPE == MediaTypes.PHOTO:
            # TODO replace PhotoLoader
            self.source = VideoLoader.getInstance()

    @classmethod
    def getSource(cls):
        return cls.getInstance().source
class Singleton():
    __instance = None

    # @classmethod
    # def __getInstance(cls):
    #     return cls.__instance

    @classmethod
    def getInstance(cls, *args, **kargs):
        if cls.__instance is None:
            cls.__instance = cls(*args, **kargs)
        # cls.__instance = cls(*args, **kargs)
        # cls.instance = cls.__getInstance
        return cls.__instance
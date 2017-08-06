class Singleton():
    __instance = None

    @classmethod
    def getInstance(cls, *args, **kargs):
        if cls.__instance is None:
            cls.__instance = cls(*args, **kargs)

        return cls.__instance
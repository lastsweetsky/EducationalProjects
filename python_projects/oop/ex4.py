class Point:
    MIN_COORD = 0
    MAX_COORD = 100

    def __init__(self, x=0, y=0):
            self.x = x
            self.y = y

    def set_coord(self, x, y):
        if self.MIN_COORD <= x <= self.MAX_COORD:
            self.x = x
            self.y = y

    def __getattribute__(self, item):
        if item == 'x':
            raise ValueError('forbidden')
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == 'z':
            raise AttributeError ("no z in da club")
        else:
            #object.__setattr__(self,key,value)
            self.__dict__[key] = value

    def __getattr__(self, item):
        return False

    def __delattr__(self, item):
        print("dell" + item)
        object.__delattr__(self,item)

pt1 = Point(1, 2)
pt2 = Point(10, 20)
pt1.y = 5
del pt1.x
print(pt1.__dict__)

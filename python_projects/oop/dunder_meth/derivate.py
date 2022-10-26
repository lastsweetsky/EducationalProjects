import math


class Derivate:
    def __init__(self, function):
        self.__fn = function

    def __call__(self, x, dx=0.0001, *args, **kwargs):
        return (self.__fn(x + dx) - self.__fn(x)) / dx


def df_sin(x):
    return math.sin(x)


df_sin = Derivate(df_sin)
print(df_sin(math.pi / 3))

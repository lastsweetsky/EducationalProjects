class Counter:
    def __init__(self):
        self.__counter = 0

    def __call__(self,step=1, *args, **kwargs):
        print("__call__")
        self.__counter += step
        return self.__counter

c = Counter()
c2 = Counter()
c()
c(2)
res = c(10)
res2 = c2(-5)
print(res,res2)
class Point:
    color = 'red'
    circle = 2

    def __init__(self,x=0,y=0):
        print("initialization")
        self.x = x
        self.y = y

    def __del__(self):
        print('finalization')

    def set_coords(self,x,y):
        self.x = x
        self.y = y

    def get_coords(self):
        return (self.x, self.y)


pt = Point(1)
print(pt.__dict__)
# pt2 = Point()
# pt.set_coords(1,2)
# pt2.set_coords(10,20)
# f = getattr(pt,'get_coords')
# print(f())
# print(pt.get_coords())
# print(pt2.get_coords())
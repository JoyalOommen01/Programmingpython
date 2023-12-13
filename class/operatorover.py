class rectangle:
    def __init__(self):
        self.__length=int(input("enter the length: "))
        self.__breadth=int(input("enter the length: "))
        self.area=self.__length*self.__breadth
    def greaterthan(self,rectangle):
        if self.area<rectangle.area:
            print("area of rectangle1 is greater")
        else:
            print("area of rectangle2 is greater")
print("rectangle 1")
r1=rectangle()
print("rectangle 2")
r2=rectangle()
print("comparing Rectangle:")
r2.greaterthan(r2)
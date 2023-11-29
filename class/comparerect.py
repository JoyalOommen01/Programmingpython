class rectangle:
    def __init__(self,length,width):
        self.len=length
        self.wid=width
    def calc_area(self):
        self.area=self.len*self.wid
        print("area is :", self.area)
        return(self.area)
    def calc_peri(self):
        self.peri=2*(self.len + self.wid)
        print("perimeter is :", self.peri)
length1 = int(input("Enter the length of the first rectangle"))
width1 = int(input("Enter the breadth of the first rectangle"))
length2 = int(input("Enter the length of the second rectangle"))
width2 = int(input("Enter the breadth of the second rectangle"))
obj1=rectangle(length1, width1)
obj2=rectangle(length2, width2)
r1=obj1.calc_area()
r2=obj2.calc_area()
obj1.calc_peri()
obj2.calc_peri()
if r1 > r2:
    print("rectangle one is larger")
else:
    print("rectangle two is larger")

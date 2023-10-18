list1=[]
len1=int(input("enter the number elements you want to add o list"))
for i in range (0,len1):
    print("enter the element",i+1)
    inp=int(input())
    list1.append(inp)
s=0
for i in list1:
    s=s+i
print("sum of the elements in the list are",s)

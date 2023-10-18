a=int(input("enter the first number in the series"))
b=int(input("enter the second number in the series"))
n=int(input("enter the number of terms to be needed"))
print("fibanocci series")
print(a,b,"\n")
for i in range (2,n+1):
    f=a+b
    a=b
    b=f
    print(f,"\t")

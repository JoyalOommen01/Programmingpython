a=0
b=1
n=int(input("enter the number of terms to be needed"))
print("fibanocci series")
if(n==0 or n==1):
  print(a)  
else:
      print(a)
      print(b)
      for i in range (2,n):
        f=a+b
        a=b
        b=f
        print(f,"\t")

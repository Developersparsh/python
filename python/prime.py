n=int(input("enter any number"))
s=0
for i in range(2,n-1,1):
    if(n%i==0):
        s=s+1
        break
    if(s==0):
        print("prime number")
    else:
        print("not prime number")
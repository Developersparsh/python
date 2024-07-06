n=int(input("enter any number:"))
s=0
x=n
while n>0:
    r=n%10
    s=s+10*r
    n=n//10
    if(s==n):
        print("pallindrome")
    for i in range(2,n-1,1):
        if(i%x==0):
            s=s+1
            break
    if(s==x):
        print("prime number")
    elif:
    print("not prime")
else:
    print("not pallindrome")   
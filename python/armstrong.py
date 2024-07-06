n=int(input("enter any number:"))
s=0
x=n
while n>0:
    r=n%10
    s=s+r*r*r
    n=n//10
if(s==x):
    print("armstrong number")
else:
    print("not armstrong")
percentage=float(input("enter the student percentage"))
if 40<=percentage<60:
    print("second division")
elif 60<=percentage<75:
    print("first division")
elif 75<=percentage<=100:
    print("first division with honor")
else:
    print("fail")
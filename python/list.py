list1=list()
l2=list([10,20,30])
print(l2)
l3=list(["apple","grapes","banana"])
print(l3)
l4=list(range(0,6))
print(l4)
l5=list("abc")
print(l5)
l6=['python','programming,',2310,4491]
print(l6)
print(l2[1])
print(l2[0])
print(l3[2])
print(l4[-1])
print(l4[-2])

list4=["first","list item",21,4,5,25]
list5=["this","is","another","list"]
print(list4)
print(list4[1:4])
print(list4[0:5:2])
print(list5[::-1])
print(list4[-1:0:-1])
print(list4[0])
print(list4[:-2])
print(list4*1)
print(list4+list5)

import random
list6=["second","list item",2,7,66,55]
list7=[1,2,3,4,5,6,7]
print(len(list6))
print(max(list7))
print(min(list7))
print(sum(list7))
random.shuffle(list7)
print(list7)

list7.append(24)
print(list7)
list6.extend(list7)
print(list6)
list1=[1,2,3]
list1[1]=100
print(list1)

list2=[10,20,30]
list2[-1]=50
print(list2)

list3=[1,2,3,4,5]
list3[1:4]=[100,200,300]
print(list3)

list4=[1,2,3,4,5]
for i in range(len(list4)):
    print(list4[i])

list5=[1,2,3,4,5,6,7,8,9,10]
print([x*2 for x in list5])

list1.remove(3)
print(list1)

list2.pop(1)
print(list2)

list3.clear()   
print(list3)

del list4
print(list4)

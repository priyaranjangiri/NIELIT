#packing in tuple
tpl=(1,2,3,41,5)
a=1
b=2
c=3
d=41
e=5
for x in range(len(tpl)):
    print(tpl[x])

for x in tpl:
    print(x)

a,b,c,d,e=tpl   
print(a,b,c,d,e)

#Update and delete in tuple
#tuple is immutable, we cannot update or delete the elements of tuple but we can delete the entire tuple

tpl[1]=100
print(tpl)

del tpl[1]
print(tpl)

del tpl
print(tpl)
#positional argument
def add(a,b):
    print("positional:",a+b)
add(10,20)

#keyword argument
def display(name,age):
    print("keyword: ",name,age)
display(age=25,name="amit")

#default argument
def greet(name="Guest"):
    print("default: Hello",name)
greet()

#variable length argument
def total(*nums):
    print("args:",nums)
total(1,10,21)

#keyword variable length argument
def info(**data):
    print("kwargs:",data)
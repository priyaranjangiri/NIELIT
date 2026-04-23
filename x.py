f=("exclusive.txt","x")
f.close()

f=open("exclusive.txt","w")
f.write("This is an exclusive file")
f.close()

f=open("exclusive.txt","r")
print(f.read())
f.close()
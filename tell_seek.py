f=open("example.txt","r")
print(f.tell())

print(f.read(4))

f.seek(0)
print(f.read())

f.close()
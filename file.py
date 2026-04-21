#read the prior content of the file
f=open("demo.txt","r")
print(f.read())
f.close()

#write to the file
#it over write the prior content of the file
f=open("demo.txt","w")
f.write("this the first line\n")
f.write("this the second line\n")
f.close()

#new content of the file
f=open("demo.txt","r")
print(f.read())
f.close()

#append to the file
f=open("demo.txt","a")
f.write("this the third line\n")
f.close()

#new content of the file
f=open("demo.txt","r")
print(f.read())
f.close()

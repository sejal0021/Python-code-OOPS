f1=open("HELLO.txt",'w')
f1.write("WELCOME TO PYTHON")#use to print this in hello.txt file
f1.close()
f1=open("HELLO.txt",'a')#append
f1.write("HOW ARE YOU?")
f1.close()
f1=open("HELLO.txt",'r')
f1.seek(5)
print(f1.read(10))
print(f1.read())
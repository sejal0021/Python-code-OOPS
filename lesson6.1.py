f1=open("HELLO.txt",'w')
f1.write("WELCOME TO PYTHON")#use to print this in hello.txt file
f1.close()
f1=open("HELLO.txt",'r')
print(f1.read())# use to read 
print(f1.tell())#to check where is the cursor #ans=17
print(f1.read())#its already readed so no output here
f1.close()
f1=open("HELLO.txt",'r')# to read few bit position
print(f1.read(4))
print(f1.read(5))
print(f1.read(2))
print(f1.read())
print(f1.read())
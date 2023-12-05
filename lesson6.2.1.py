f1=open("HELLO011.txt",'r')
f2=open("NewData11.txt",'w')
for i in f1:
    f2.write(i)
f1.close()
f2.close()
f2=open("NewData11.txt",'r')
print(f2.read())
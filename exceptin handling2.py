a=10
b=0
l1=[10,20,30,40,50]
try:
    c=a/b
    print(c)
    print(l1[7])
except ZeroDivisionError:
    print("Exception raised using default value for den")
    b=1
    c=a/b
    print(c)

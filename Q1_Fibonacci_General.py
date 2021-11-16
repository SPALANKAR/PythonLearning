'''
Fibonacci Series using range 
'''

a=1
b=1
record = int(input("Enter Value \n"))
print(a)
print(b)


for i in range(2,record):
    c=a+b
    a=b
    b=c
    print(c)



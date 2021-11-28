'''
Fibonacci Series
'''

a=1
b=1
print(a)
print(b)
count=0
while count < 3:
    a=a+b
    print(a)
    b=a+b
    print(b)
    count+=1
else:   
    b=a+b
    print(b)



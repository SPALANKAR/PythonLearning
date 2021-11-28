'''
To check the number is in Fibonacci Series
'''

a=1
b=1
print(a)
print(b)
sequence = [1]
count=0
while count < 3:
    a=a+b
    print(a)
    sequence.append(a)
    b=a+b
    print(b)
    sequence.append(b)
    count+=1
values=int(input("Provide a number to check if the number is fibonacci or not \n"))
if values in sequence:
    print(values,'is a fibonacci number')
else:
    print(values,'is not a fibonacci number')
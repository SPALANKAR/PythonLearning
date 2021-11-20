'''
    Identifying the Grade of the student
'''

print("Marks for English,Science and Maths should be less than 100")
eng = int(input("Enter marks for English \n"))
sci = int(input("Enter marks for Science \n"))
math = int(input("Enter marks for Maths \n"))

percentage = int(((eng+sci+math)*100)/300)
print("Percentage of the student is",percentage)

if eng >= 35 and sci >= 35 and math >= 35:
    if percentage >= 90:
        print("Student has passed with Grade A")
    elif percentage >=80 and percentage <= 89:
        print("Student has passed with Grade B")
    else :
        print("Student has passed with Average Marks")
else:
    print("Student has failed with marks less than 35 in one of the subject")

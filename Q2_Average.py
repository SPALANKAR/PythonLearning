'''
Find the average number of marks scored by this batch of student in the list marks.
'''


marks = [78,89,85,91,93,82,79]
counts=len(marks)    #Identifying the records present in the list
total=sum(marks)     #Addition of records present in the list
Average = int(total / counts)   #Identifying the Average
print("Average marks scored by this batch of student in the list is",Average)  #Print the records

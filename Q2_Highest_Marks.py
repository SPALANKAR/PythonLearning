'''
Identify the highest and the lowest values present in the list
'''

marks = [78,89,85,91,93,82,79]

highest=max(marks)   #Identifying the max values in the list
lowest=min(marks)    #Identifying the MIN values in the list

highest_i=(marks.index(highest)+1) #Identifying the roll number of highest value
lowest_i=(marks.index(lowest)+1) #Identifying the 1th roll number of lowest value

print("Roll number of the the highest values scored student is",highest_i)
print("Roll number of the the lowest values scored student is",lowest_i)

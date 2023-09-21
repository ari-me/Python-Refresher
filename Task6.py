#TASK6
#print specified list after removing 0th, 4th, and 5th element

list = ['red', 'pink', 'purple', 'yellow', 'orange', 'green']
list = [x for (i,x) in enumerate(list) if i not in (0,4,5)]
print(list)
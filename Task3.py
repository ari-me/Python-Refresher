#TASK3
#Convert tuple to a dictionary

#Convert two tuples into one dictonary
tuple1 = ("apple", "banana", "mango")
index = (1, 2, 3)
dictionary1 = dict(zip(index, tuple1))
print(dictionary1)

#Convert a tuple of nested tuples into one dictionary
tuple2 = ((1, "apple"),(2, "banana"), (3,"mango"))
dictionary2 = dict((x,y)for x,y in tuple2)
print(dictionary2)
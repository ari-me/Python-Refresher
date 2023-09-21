#TASK4
#sort tuple by its float element

#Sorting a tuple using sorted 
tuple = (2.2, 4.5, 1.1)
sort = sorted(tuple)
print(sort)

#Sorting a tuple by transforming it inot a list
sorted_list = list(tuple)
sorted_list.sort()
print(sorted_list)

#Sorting a nested tuple
nested_tuple = [('itm1', '2.20'), ('itm2','1.10'), ('itm3','4.5')]
nested_tuple.sort(key = lambda x : x[1])
print(nested_tuple)
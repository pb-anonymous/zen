def calculate_average(lst): 
	total = sum(lst) 
	number_of_items = len(lst) 
	return total / number_of_items 

numbers = [1, 2, 3, 4, 5] 
print(calculate_average(numbers))
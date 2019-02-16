def validate(n):
	n_list = [int(x) for x in str(n)]
	doubled_list = list()
	# Even
	if len(n_list) % 2 == 0:
		doubled_list = [x*2 if index % 2 != 0 else x for index, x in enumerate(n_list, 1)]
	# Odd
	else:
		doubled_list = [x*2 if index % 2 == 0 else x for index, x in enumerate(n_list, 1)]

	cleaned_list = [int(str(x)[0]) + int(str(x)[1]) if x > 9 else x for x in doubled_list]
	return sum(cleaned_list) % 10 == 0
		
print(validate(input('Input Credit Card Number')))

# Passed	

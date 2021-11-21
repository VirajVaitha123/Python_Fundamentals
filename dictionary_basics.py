## Dictionaries

# Create dictionary
my_dict = {'apple':2.99,'oranage':2}

# show price of apple
print(my_dict['apple'])

# dictionaries can contain lists or another dictionart
my_dict = {'key1':10,'key2':[20,30,40], 'key3':{'insideKey':30}}
print(my_dict['key2'])
print(my_dict['key2'][0])
print(my_dict['key3'])
print(my_dict['key3']['insideKey'])

# return keys and values
print(my_dict.keys())
print(my_dict.values())
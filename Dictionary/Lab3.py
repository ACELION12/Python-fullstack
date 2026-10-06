"""Write a Python program to get the key, value and item in a dictionary.
input:dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}"""

dict_num = {'1': 10, '2': 20, '3': 30, '4': 40, '5': 50, '6': 60}
key = dict_num.keys()
value = dict_num.values()
item = dict_num.items()
print( key, '\n', value, '\n', item)
input_dict = {'1':10,'2':20,'3':None,'4':40,'5':None,'6':60}
items = {key: value for key, value in input_dict.items() if value is not None} # This is the main line where we are removing the None values and retriving the rest.
print(items)
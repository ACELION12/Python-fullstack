'''Write a Python program and calculate the mean of the below dictionary.
test_dict = {"A" : 6, "B" : 9, "C" : 5, "D" : 7, "E" : 4}
Output: 6.2'''

test_dict = {"A":6,"B":9,"C":5,"D":7,"E":4}
x = test_dict.values() #this to retrive all the values 
y = len(test_dict) #to get the total number of items 
mean = sum(x) / y #formula for mean 
print(mean)
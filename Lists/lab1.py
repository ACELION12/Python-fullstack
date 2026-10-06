'''Write a Python program to count the occurrences of each word in a given sentence string = “To change the overall look of your document. To change the look available in the gallery”
'''
string = "To change the overall look of your document To change the look available in the gallery"

words = string.split() #splitting each word 

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)
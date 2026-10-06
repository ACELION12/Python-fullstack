#write a Python program to count the occurrences of each word in a given sentance.
'''Sentance = "To chanage the overall look of your document, To change the look available in the gallery." 
words = Sentance.split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word occurrences:")
for word, count in word_count.items():
    print(word, ":", count)'''


'''Sentance = "To chanage the overall look of your document, To change the look available in the gallery." 
string1=''
for word in Sentance.split():
    if word not in string1:
        string1+=word+''
    else:
        print(word,'=',Sentance.count(word))
print(string1)'''




#Write a Python program to reverse words in a string.
string = "Deeptech Python Training"

words = string.split()

for word in words:
    print(word[::-1], end=" ")

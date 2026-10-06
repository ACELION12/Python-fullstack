string = "Deeptech Python Training"

words = string.split() #split the words

for word in words:
    print(word[::-1], end=" ")
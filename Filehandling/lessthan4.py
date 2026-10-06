def display_words():
    with open('Filehandling/one.txt', 'r+') as file1:
        content = file1.read()
        print(content)
        for word in content.split(): #splits the words in file
            if len(word) < 4:# extracts the words that are less than 4 in length
                print(word)
display_words()


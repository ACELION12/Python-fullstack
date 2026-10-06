with open('Filehandling/one.txt','r+') as file1:
    lines=file1.read().split() #splits the words into list format.
    print(lines)#prints the words.
    count = len(lines)
    print("total number of words",count)#counts and gives us the total number of words.
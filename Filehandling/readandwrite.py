with open('Filehandling/one.txt','r+') as file1:
    lines=file1.readlines()
    for line in lines:
        print(line)
    file1.write('hello world.\npython id interpreted language')
    print('written to a file')

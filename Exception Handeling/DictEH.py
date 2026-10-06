'''student = {
    "1234": "Sathwik",
    "4321": "Rahul",
    "": "Suraj"
}
id=student.get("")
print(id)'''


'''student = {
    "1234": "Sathwik",
    "4321": "Rahul",
    "5678": "Suraj"
}

id = int(input("Enter Student id : "))

try:
    print(student[id])

except Exception as E:
    if type(E).__name__ == "KeyError":
        print("Student ID does not exist.")

    elif type(E).__name__ == "ValueError":
        print("Please enter a valid ID.")

    else:
        print("Some other error occurred.")'''
    


student = {
    "1234": "Sathwik",
    "4321": "Rahul",
    "5678": "Suraj"
}

try:
    id = int(input("Enter Student id : "))
    print(student[id])

except Exception as E:
    if isinstance(E, KeyError):
        print("Student ID does not exist.")

    elif isinstance(E, ValueError):
        print("Please enter a valid ID.")

    else:
        print("Some other error occurred.")
def write_file():
    with open('Filehandling/student_data.txt', 'a+') as file1:

        x = int(input("Enter the number of entries: "))

        for student in range(x):
            student_id = int(input("Enter student id: "))
            student_name = input("Enter student name: ")

            file1.write(
                f"student_id: {student_id} student_name: {student_name}\n"
            )

        print("Written to the file successfully.")


write_file()

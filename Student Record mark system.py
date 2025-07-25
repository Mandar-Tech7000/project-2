students = {}

while True:
    print("\n1. Add Student\n2. View All\n3. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        name = input("Student name: ")
        marks = float(input("Marks: "))
        students[name] = marks
    elif choice == '2':
        for name, mark in students.items():
            print(f"{name} : {mark}")
    elif choice == '3':
        break
    else:
        print("Invalid choice")

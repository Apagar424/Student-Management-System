students = []
while True:
print("\n===== Student Management System =====")
print("1. Add Student")
print("2. View Students")
print("3. Search Student")
print("4. Delete Student")
print("5. Exit")

choice = input("Enter your choice: ")  

if choice == "1":  
    roll = input("Enter Roll Number: ")  
    name = input("Enter Student Name: ")  
    marks = input("Enter Marks: ")  

    student = {  
        "roll": roll,  
        "name": name,  
        "marks": marks  
    }  

    students.append(student)  
    print("Student Added Successfully!")  

elif choice == "2":  
    if len(students) == 0:  
        print("No Students Found!")  
    else:  
        print("\n===== Student Records =====")  
        for student in students:  
            print("Roll No:", student["roll"])  
            print("Name:", student["name"])  
            print("Marks:", student["marks"])  
            print("------------------")  

elif choice == "3":  
    search_name = input("Enter Student Name to Search: ")  

    found = False  

    for student in students:  
        if student["name"].lower() == search_name.lower():  
            print("\nStudent Found!")  
            print("Roll No:", student["roll"])  
            print("Name:", student["name"])  
            print("Marks:", student["marks"])  
            found = True  

    if not found:  
        print("Student Not Found!")  

elif choice == "4":  
    delete_name = input("Enter Student Name to Delete: ")  

    found = False  

    for student in students:  
        if student["name"].lower() == delete_name.lower():  
            students.remove(student)  
            print("Student Deleted Successfully!")  
            found = True  
            break  

    if not found:  
        print("Student Not Found!")  

elif choice == "5":  
    print("Thank You!")  
    break  

else:  
    print("Invalid Choice!")

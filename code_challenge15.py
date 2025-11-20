import os
import json
os.system('cls')

print("STUDENT INFORMATION SYSTEM")
print("++++++++++++++++++++++++++")

student_record = {}

while True:
    print("SELECT FROM THE FOLLOWING OPTIONS.")
    print("A - Add Student Record")
    print("B - Print Student Record")
    print("C - Search Student Record")
    print("D - Delete Student Record")
    print("E - Edit Student Record")
    print("F - Export Student Record")
    print("G - EXIT SYSTEM")
    
    choice = input("SELECT FROM THE OPTION ABOVE: ").lower()
    
    # ADD RECORD
    if choice == 'a':
        os.system('cls')
        print("\nADDING STUDENT RECORD")
        
        id_no = input("Please Input Student ID number: ")
        
        first_name = input("First Name: ").upper()
        surname = input("Surname: ").upper()
        age = input("Age: ")
        course = input("Course: ").upper()
        section = input("Section: ").upper()
        print("")
        
        student_record[id_no] = [first_name, surname, age, course, section]
        print("DATA SUCCESSFULLY SAVED")
        print("")
        continue
        
    # PRINT RECORDS
    elif choice == 'b':
        os.system('cls')
        print("PRINTING STUDENT RECORD")
        
        for i, j in student_record.items():
            print(f"CODE - {i} - INFORMATION - {j}")
            print("")
        continue
    
    # SEARCH RECORD
    elif choice == 'c':
        os.system('cls')
        search_id = input("ID number to Search: ")
        if search_id in student_record:
            print(f"CODE - {search_id} - {student_record[search_id]}")
            print("")
        else:
            print("Student ID not found.")
        continue
    
    # DELETE RECORD
    elif choice == 'd':
        os.system('cls')
        search_id = input("ID number to Delete: ")

        if search_id in student_record:
            print(f"CODE - {search_id} - {student_record[search_id]} - STUDENT DATA SUCCESSFULLY DELETED.")
            student_record.pop(search_id)
            print("")
            
        else:
            print("Student ID not found.")
        continue
    
    # EDIT RECORD
    elif choice == 'e':
        os.system('cls')
        search_id = input("ID number to Search: ")
        if search_id in student_record:
            print("CURRENT RECORD:")
            print(student_record[search_id])
            print("=======================================")
        
            first_name = input("First Name: ").upper()
            surname = input("Surname: ").upper()
            age = input("Age: ")
            course = input("Course: ").upper()
            section = input("Section: ").upper()
            
            student_record[search_id] = [first_name, surname, age, course, section]
            
            print("DATA SUCCESSFULLY UPDATED.")
            print("")
        else:
            print("Student ID not found.")
        continue
    
    # EXPORT TO JSON
    elif choice == 'f':
        os.system('cls')
        print("EXPORT STUDENT DATA")
    
        with open('student_records.json', 'w') as new_file:
            json.dump(student_record, new_file, indent=4)
        print("DATA EXPORTED SUCCESSFULLY.")
        print("")
        continue
    
    # EXIT
    elif choice == 'g':
        print("SYSTEM EXIT")
        break

    else:
        print("INVALID INPUT. Please try again.")
        continue

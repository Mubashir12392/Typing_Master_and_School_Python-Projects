#all functions here
import os
all_data = [
    {'f_name': 'Mubashir', 
            'l_name': 'Haider', 
            'class': 'BSCS', 'dofbirth': 
            '28/10/2003', 
            'roll': '23', 
            'fee': '25000'}, 
{'f_name': 'Ali Raza', 
'l_name': 'Yameen', 
'class': 'BBA', 
'dofbirth': 
'5/10/2000', 
'roll': '25', 
'fee': '35000'},
{'f_name': 'Usman', 
'l_name': 'Malik', 
'class': 'BSCS', 
'dofbirth': '26/10/2002', 
'roll': '27', 
'fee': '12000'}
]
def main_menu ():
    os.system('cls')
    print("*********** OXFORD UNIVERSITY *************")
    print("*"*20)
    print("1: View All Students")
    print("2: Add New Student")
    print("3: Edit a student")
    print("4: Expell a student")
    print("5: Search a student")
    print("0: Exit")
    
def choice ():
    choice = int(input("Enter your Choice: "))
    if choice == 1:
        view_all_students ()
    elif  choice == 2:
        add_new_student ()
    elif choice == 3:
        edit_student ()
    elif choice == 4:
        expell_student ()
    elif choice == 5:
        search_student ()
    elif choice == 0:
        exit()
    else:
        print("Invalid Choice")

def view_all_students ():
    os.system('cls')
    for elements in all_data:
        print(f"{elements['roll']} - {elements['f_name']} - {elements['l_name']} - {elements['class']} - {elements['fee']}")
        print()
    input("Press any key to go Back")

def add_new_student ():
    os.system('cls')
    first_name = input ("Enter your First Name: ")
    last_name = input ("Enter your Last name: ")
    class_ = input ("Enter you Class: ")
    dob_ = input ("Enter your Date of Birth: ")
    roll_ = input ("Enter Your Roll Number: ")
    fees_ = input ("Enter your Fee: ")
     
     
    student = {
            'f_name' : first_name,
            'l_name' : last_name, 
            'class' : class_,
            'dofbirth' : dob_,
            'roll' : roll_,
            'fee' : fees_}
    
    all_data.append(student)
    os.system('cls')
    print(f"The Student {student['f_name']} is added Successfully ")
    input("Press any key to go Back")

def edit_student():
    os.system('cls')
    given_roll = input("Enter Roll Number: ")
    x = 0
    for students in all_data:
        if  all_data[x]['roll'] == given_roll:
            while True:
                os.system('cls')
                print("********************** Here is your Data *****************************")
                print()
                print(f" Name: {all_data[x]['f_name']} {all_data[x]['l_name']} -- Class: {all_data[x]['class']} --DOB: {all_data[x]['dofbirth']} -- Roll No: {all_data[x]['roll']} -- Fees: {all_data[x]['fee']}")
                print()
                print("Which Element You want to Change:")
                print()
                print("1: First Name")
                print("2: Last Name")
                print("3: Class")
                print("4: DOB")
                print("5: Roll No")
                print("6: Fee")
                print("0: Exit")
                choice_ =int(input("Enter Your Choice: "))
                if choice_ == 1:
                    os.system('cls')
                    new_f_name = input("Enter Your New First Name: ")
                    all_data[x]['f_name'] = new_f_name
                    print(" YOUR FIRST NAME HAS BEEN CHANGED SUCCESSFULLY")
                    input("Press any Key to Go Back")
                elif choice_ == 2:
                    os.system('cls')
                    new_l_name = input("Enter Your New Last Name: ")
                    all_data[x]['l_name'] = new_l_name
                    print(" YOUR LAST NAME HAS BEEN CHANGED SUCCESSFULLY")
                    input("Press any Key to Go Back")
                elif choice_ == 3:
                    os.system('cls')
                    new_class_name = input("Enter Your New Class Name: ")
                    all_data[x]['class'] = new_class_name
                    print(" YOUR CLASS HAS BEEN CHANGED SUCCESSFULLY")
                    input("Press any Key to Go Back")
                elif choice_ == 4:
                    os.system('cls')
                    new_dob = int(input("Enter Your New Date of Birth: "))
                    all_data[x]['dofbirth'] = new_dob
                    print(" YOUR DATE OF BIRTH HAS BEEN CHANGED SUCCESSFULLY")
                    input("Press any Key to Go Back")
                elif choice_ == 5:
                    os.system('cls')
                    new_roll = int(input("Enter Your New Roll Number: "))
                    all_data[x]['roll'] = new_roll
                    print(" YOUR ROLL NUMBER HAS BEEN CHANGED SUCCESSFULLY")
                    input("Press any Key to Go Back")
                elif choice_ == 6:
                    os.system('cls')
                    new_fee = int(input("Enter Your New Fee: "))
                    all_data[x]['fee'] = new_fee
                    print(" YOUR FEE HAS BEEN CHANGED SUCCESSFULLY")
                    input("Press any Key to Go Back")
                elif choice_ == 0:
                    os.system('cls')
                    break
                else:
                    os.system('cls')
                    print("Invalid Choice")

        x += 1

def expell_student ():
    os.system('cls')
    for_expel = (input("Enter Roll Number: "))
    x = 0
    for students in all_data:
     if  all_data[x]['roll'] == for_expel:
        os.system('cls')
        print(" Here is your Data ")
        print()
        print(f" Name: {all_data[x]['f_name']} {all_data[x]['l_name']} -- Class: {all_data[x]['class']} --DOB: {all_data[x]['dofbirth']} -- Roll No: {all_data[x]['roll']} -- Fees: {all_data[x]['fee']}")
        print()
        student_want = input(" Do you Want to Expell that Student (Y/N): ")
        if student_want == 'y':
            os.system('cls')
            all_data.pop(x)
            print(f"Roll Number : {for_expel} has been Expelled")
            input("Press any Key to Go Back")
        elif student_want == 'n':
            os.system('cls')
            print("Ok")
            input("Press any Key to Go Back")
            break
        else:
            os.system('cls')
            print("Invalid Choice")
            input("Press any Key to Go Back")
     
     x += 1

def search_student ():
    os.system('cls')
    search = input("1: Search by Roll Number: ")
    x = 0
    for students in all_data:
     if  all_data[x]['roll'] == search:
        os.system('cls')
        print("**********************   Here is your Data   *****************************")
        print()
        print(f" Name: {all_data[x]['f_name']} {all_data[x]['l_name']} -- Class: {all_data[x]['class']} --DOB: {all_data[x]['dofbirth']} -- Roll No: {all_data[x]['roll']} -- Fees: {all_data[x]['fee']}")
        input("Press any Key to Go Back")
    
     x += 1
    


   
    
               
 
    
        
        
                   
    
    


    













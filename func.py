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
'fee': '35000'}
]
def main_menu ():
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
        all_students ()
    elif  choice == 2:
        new_student ()
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
def all_students ():
    for elements in all_data:
        print(f"{elements['roll']} - {elements['f_name']} - {elements['l_name']} - {elements['class']} - {elements['fee']}")
def new_student ():
    first_name = input ("Enter your first Name: ")
    last_name = input ("Enter your last name: ")
    class_ = input ("Enter you Class: ")
    dob_ = input ("Enter your Date of Birth: ")
    roll_ = input ("Enter Your Roll Number: ")
    fees_ = input ("Enter your Fee:")
     
     
    student = {
            'f_name' : first_name,
            'l_name' : last_name, 
            'class' : class_,
            'dofbirth' : dob_,
            'roll' : roll_,
            'fee' : fees_}
    
    all_data.append(student)
    
    print(f"{student['f_name']} is added Successfully ")
def edit_student():
    input("Enter Roll Number: ")
def expell_student ():
    input("Enter Roll Number: ")
def search_student ():
    input("1: Search by first name: ") 
    input("2: Search by last name: ")
    input("3: Search by roll number name: ")
    input("4: Search by class:")










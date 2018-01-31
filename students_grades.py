import statistics

admins = {'Python':'Pass123@', 'user':'user'}

studentDict = {'Jeff':[25,43,18],
               'Alex':[34,56,11],
               'Sam':[13,36,15]
               }

def enter_grades():
    nameToEnter = input('Student name: ')
    gradeToEnter = input('Grade: ')

    if nameToEnter in studentDict:
        print('Adding Grade...')
        studentDict[nameToEnter].append(float(gradeToEnter))
    else:
        print('Student does not exist.')

    print(studentDict)

def remove_student():
    nameToRemove = input('What student to remove? ')
    if nameToRemove in studentDict:
        print('removing student ... ')
        del studentDict[nameToRemove]
    else:
        print('no such student ... ')

    print(studentDict)

def compute_mean():
    for student in studentDict:
        gradeList = studentDict[student]
        avgGrade = statistics.mean(gradeList)
        print(student,"has avg grade:", avgGrade)

def main():
    # print multiline
    print("""
        Welcome to Grade Central
        
        [1] - Enter Grades
        [2] - Remove Student
        [3] - Student Average Grades
        [4] - Exit
    """)
    print(studentDict)
    action = input("What would you like to do? (Enter e number): ")
    if action == '1':
        enter_grades()
    elif action == '2':
        remove_student()
    elif action == '3':
        compute_mean()
    elif action == '4':
        exit(0)
    else:
        print('No valid choice was given, try again')

login = input("Login: ")
password = input("Password: ")

if login in admins:
    if admins[login] == password:
        print('Welcome, ',login)
        while True:
            main()
    else:
        print('Invalid password')
else:
    print('Invalid login')



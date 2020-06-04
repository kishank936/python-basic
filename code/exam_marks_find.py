# PYTHON PROGRESS - Exam  Marks

exam_marks= {'jake':'A', 'jack':'B' ,'jane':'C'}

print('ENTER A NAME OF A PERSON YOU WANT TO CHECK MARKS')

person_name = input('Name:  ')
if person_name == None:
    exit()

if person_name in exam_marks:
    print('Exam marks ' + person_name +   'is' + exam_marks[person_name])
else:
    print('cant find results for ' + person_name)

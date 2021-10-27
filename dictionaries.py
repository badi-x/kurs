student = {'name': ' John', 'age': 25, 'courses': ['Math', 'CompSci']}

student.update({'name': 'Jane', 'age': 26, 'phone': 555-5555})
# print(student.get('phone', 'Not Found'))
# del student['age']
# student['phone'] = '555-55555'
# print(student.get('phone', 'Not Found'))

print(student)

for key, value in student.items():
print(key, value)

courses = ['History', 'Math', 'Physics', 'CompSci']
courses_2 = ['Education', 'Art']
courses.insert(3, 'language')

courses.extend(courses_2)
popped = courses.pop()
courses.sort()
print(popped)
print(courses)

nums = [1, 5, 2, 4, 3, 7, 11]
nums.sort(reverse=False)
print(nums)

for index, course in enumerate(courses, start=1):
    print(index, course)

course_str = ' - '.join(courses)
print(course_str)

new_list = course_str.split(' - ')
print(new_list)

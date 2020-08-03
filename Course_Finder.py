import pandas as pd

course_dict = {"Griffith Park - Harding": 5997, "Griffith Park - Wilson": 5998, \
"Hansen Dam": 5995, "Harbor Park": 5996, \
"Los Feliz": 17679, "Penmar": 6171, "Rancho Park": 6204, "Rancho Park - Par 3": 6205, \
"Roosevelt": 6226, "Sepulveda - Balboa": 6264, "Sepulveda - Encino": 6263, "Woodley Lakes": 6380}

value_course_dict = {value : key for (key,value) in course_dict.items()}

def courseFinder(*value, byID = False):
    if byID == True:
        for x in value:
            print(value_course_dict[x])
    else:
        for x in value:
            print(course_dict[x])

def show_courses():
    print(course_dict)

if __name__ == '__main__':
    show_courses()
    #courses = input('\nWhich courses would you like to see?')
    #id = input("Search by id? (y/n)")
    #if id == 'y':
    #    courseFinder(courses, byID = True)
    #else:
    #    courseFinder(courses, byID = False)

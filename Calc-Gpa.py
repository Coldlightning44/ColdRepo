import os,time

class Course():
    def __init__(self,grade,credit):
        self.grade = grade
        self.credit = credit

    def calculate_grades(self):
        self.A = 5
        self.B = 4
        self.C = 3
        self.D = 2
        self.E = 1

        if self.grade.upper() == 'A':
            self.grade = self.A * self.credit

        elif self.grade.upper() == 'B':
            self.grade = self.B * self.credit

        elif self.grade.upper() == 'C':
            self.grade = self.C * self.credit

        elif self.grade.upper() == 'D':
            self.grade = self.D * self.credit

        elif self.grade.upper() == 'E':
            self.grade = self.E * self.credit

        return self.grade




def main():


    file = input(r'What is the location of your file: ')

    courses = []
    with open(file, 'r') as f:
        grades = f.read()

    grades = grades.split('\n')

    dic = {}

    for x in range(len(grades)):
        if grades[x][0] in dic.keys():
            dic[grades[x][0]].append(grades[x][2])
        else:
            dic[grades[x][0]] = list(grades[x][2])

    keys = list(dic.keys())

    for x in range(len(keys)):
        for y in range(len(dic[keys[x]])):
            course = Course(keys[x], int(dic[keys[x]][y]))
            courses.append(course)

            # print(f'{keys[x]}:{dic[keys[x]][y]}')
    final_gpa(courses)

    time.sleep(7)



def total_credits(courses):
    sum = []
    count = 0
    for course in courses:
        sum.append(course.credit)

    for x in sum:
        count += x
    return count

def total_grade(courses):
    sum = []
    count = 0
    for course in courses:
        sum.append(course.calculate_grades())

    for x in sum:
        count += x
    return count

def final_gpa(courses):
    gpa = round((total_grade(courses)) / (total_credits(courses)), 2)

    print(gpa)




if __name__ == "__main__":
    main()




import sys

def score(s):
    if s < 38:
        return s
    else:
        m_five =  s//5
        if (m_five + 1) * 5 - s >= 3:
            return s
        else:
            return (m_five + 1) * 5

def solve(grades):
    # Complete this function
    return map(lambda s:score(s), grades)

n = 4
grades = [73, 67, 38, 33]
grades_i = 0
result = solve(grades)
print "\n".join(map(str, result))




"""
HackerLand University has the following grading policy:
•Every student receives a  in the inclusive range from  to .
•Any  less than  is a failing grade. 

Sam is a professor at the university and likes to round each student's  according to these rules:wetx

Given the initial value of  for each of Sam's  students, write code to automate the rounding process. For each , round it according to the rules above and print the result on a new line.



Input Format



The first line contains a single integer denoting  (the number of students). 
    Each line  of the  subsequent lines contains a single integer, , denoting student 's grade.



Constraints


    •
•



Output Format



For each  of the  grades, print the rounded grade on a new line.



Sample Input 0



4
73
67
38
33




Sample Output 0



75
67
40
33




Explanation 0



image
1.Student  received a , and the next multiple of  from  is . Since , the student's grade is rounded to .
2.Student  received a , and the next multiple of  from  is . Since , the grade will not be modified and the student's final grade is .
3.Student  received a , and the next multiple of  from  is . Since , the student's grade will be rounded to .
4.Student  received a grade below , so the grade will not be modified and the student's final grade is .
"""

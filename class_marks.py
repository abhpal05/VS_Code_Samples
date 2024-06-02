"""

Named tuples assign meaning to each position in a tuple and allow for more readable, self-documenting code. 
They can be used wherever regular tuples are used, and they add the ability to access fields by name instead of position index.
You are given a data containing test results of class. The dataset consists of two columns namely : 'marks' and 'name'. 
These two Columns can be in any order i.e. ('name' followed by 'marks' or vice versa).
You have to find the average marks for the whole class.


Input Format
First line will contain an Integer N, denoting the number of students.
Next line will contain two string denoting the column heading.
Next N lines will contain marks and name of the students respective of column headings.


Constraints
1 <= N <= 10^3
0 <= Marks <= 100


Output Format
Output the average marks of the class rounded off to two decimal places.

"""

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    total_marks = 0
    student_count = int(input())
    a,b = input().split()
    if a == "marks":
        for _ in range(student_count):
            b,c = input().split()
            total_marks = total_marks + int(b)
    else:
        for _ in range(student_count):
            b,c = input().split()
            total_marks = total_marks + int(c)
    avg_marks = total_marks/student_count
    print("%.2f"%avg_marks)
    



main()
"""
College and Clubs (100 Marks)
There are two clubs operating in your college. The first one is a Dance club named as 'Extravenza' and the other one is a Sports club named as 'Tez'. 
Some of the students are enrolled in Extravenza, some of them are enrolled in Tez. But there is a small group of students who are enrolled in both of these clubs.
You as a representative of the student council is given a task to tell the total count of students who are enrolled in atleast one of the clubs. 

Input Format
First line will contain  an Integer N, denoting the number of students enrolled in Club Extravenza.
Next line will contain N Integers, denoting student Id's of the students enrolled in Club Extravenza.
Second line will contain  an Integer M, denoting the number of students enrolled in Club Tez.
Next line will contain M Integers, denoting student Id's of the students enrolled in Club Tez.


Constraints
1 <= N, M <= 2 * 10^2
1 <= Student Id's <= 10^3

Output Format
Output an Integer denoting the count of students who are enrolled in atleast one of the clubs.

"""

def main():
    e_count = int(input())
    e_list = list(map(int, input().rstrip().split()))
    t_count = int(input())
    t_list = list(map(int, input().rstrip().split()))
    et_list = e_list + t_list
    et_set = set(et_list)
    print(len(et_set))
main()
"""
Monk and Inversions
Monk's best friend Micro, who happen to be an awesome programmer, got him an integer matrix M of size  for his birthday. 
Monk is taking coding classes from Micro. They have just completed array inversions and Monk was successful in writing a program to count the number of inversions in an array. 
Now, Micro has asked Monk to find out the number of inversion in the matrix M. 
Number of inversions, in a matrix is defined as the number of unordered pairs of cells {{i,j},(p,q)} such that M[i][j] > M[p][q] & i<=p and j<=q.
Monk is facing a little trouble with this task and since you did not got him any birthday gift, you need to help him with this task.

Input:
First line consists of a single integer T denoting the number of test cases.
First line of each test case consists of one integer denoting N. Following N lines consists of N space separated integers denoting the matrix M.

Output:
Print the answer to each test case in a new line.
"""

test_case_number = int(input())

for i in range(test_case_number):
    matrix_size = int(input())
    matrix_input = []
    for a in range(matrix_size):
        matrix = input().split()
        matrix_int = [int(z) for z in matrix]
        matrix_input.append(matrix_int)
    
    inversion_count = 0

    for a in range(len(matrix_input)):
        for b in range(len(matrix_input)):
            for c in range(a, len(matrix_input)):
                for d in range(b, len(matrix_input)):
                    x = matrix_input[a][b]
                    y = matrix_input[c][d]
                    if(x > y):
                        inversion_count = inversion_count + 1
                        #print(str(a)+"-"+str(b)+" "+str(c)+"-"+str(d)+" "+ str(matrix_input[a][b])+ "-" + str(matrix_input[c][d]) +" "+ str(inversion_count))
                    
    
    print(inversion_count)
                        




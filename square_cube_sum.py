number_upper = int(input("Enter upper range number: "))

# 1 + 2 + 3 + 4 + .... + N
normal_sum = (number_upper * (number_upper + 1))//2
print(normal_sum)

# 1*1 + 2*2 + 3*3 + 4*4 + .. + N*N
square_sum = (number_upper * (number_upper + 1) * ((2 * number_upper) + 1))//6
print(square_sum)

# 1*1*1 + 2*2*2 + 3*3*3 + 4*4*4 + .. + N*N*N
cube_sum = pow(((square_sum * (square_sum + 1)) // 2), 2)
print(cube_sum)
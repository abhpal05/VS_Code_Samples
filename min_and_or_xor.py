
test_case = int(input())
for _ in range(test_case):
    number_count = int(input())
    number_list = list(map(int, input().rstrip().split()))
    result_list = []
    result = 100000000
    for j in range(number_count-1):
        for k in range(j+1, number_count):
            result1 = ((number_list[j]&number_list[k])^(number_list[j]|number_list[k]))
            if(result > result1):
                result =  result1
    print(result)




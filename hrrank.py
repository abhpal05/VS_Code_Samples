score_dict = {'Krishna': [67.0, 68.0, 69.0], 'Arjun': [70.0, 98.0, 63.0], 'Malika': [52.0, 56.0, 60.0]}
need_name = "Malika"

#print(need_name)
#print(score_dict)
#print(score_dict.get(need_name))  

need_list = score_dict.get(need_name)
#print(need_list)
need_list_count = len(need_list)
need_list_sum = 0
for x in need_list:
    need_list_sum += x
print(need_list_sum/need_list_count)
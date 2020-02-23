import re

def main_func():
    input_string = input()
    numbers_list = re.findall(r'\d',input_string)
    numbers_list = list(set(numbers_list))
    numbers_list.sort(reverse=True)
    maxi = ""
    for i in range(len(numbers_list)):
        maxi += numbers_list[i]
    final_list = []
    for x in range(int(maxi)):
        if x%2==0:
            final_list.append(x)
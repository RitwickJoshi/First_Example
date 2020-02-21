import re

def perform_join(number_list):
    return "".join(number_list)

def merge(even_list, odd_list):
    merged_list = []
    while True:
        try:
            merged_list.append(even_list.pop(0))
        except IndexError:
            pass
        try:
            merged_list.append(odd_list.pop(0))
        except IndexError:
            pass
        if len(even_list)==0 and len(odd_list)==0:
            break

    return merged_list

def challenge_one():
    input_string = input()
    symbols = re.findall(r'\D',input_string)
    numbers = re.findall(r'\d',input_string)
    count = len(symbols)
    final_list_even = []
    final_list_odd = []
    if count%2==0:
        pass
    else:
        for number in numbers:
            if int(number)%2==0:
                final_list_even.append(number)
            else:
                final_list_odd.append(number)

    final_list = merge(final_list_even, final_list_odd)
    print(perform_join(final_list))

challenge_one()
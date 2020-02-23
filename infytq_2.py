def sum_of_squares(number):
    tot=0
    while(number>0):
        dig=number%10
        tot=tot+dig
        number=number//10
    return tot

def Evod(number):
    if number%2 == 0:
        return 0
    return 1

def shift_right(string):
    Rfirst = string[0 : len(string)-1]
    Rsecond = string[len(string)-1 : ]
    return Rsecond+Rfirst

def shift_left(string):
    Lfirst = string[0:2]
    Lsecond = string[2:]
    return Lsecond+Lfirst

def second():
    string_input_list = input().split()
    number_input_list = list(map(int,input().split()))
    squares_list = []
    for number in range(len(number_input_list)):
        try:
            squares_list.append(sum_of_squares(number_input_list[number]))
            if Evod(squares_list[number]) == 0:
                print(shift_right(string_input_list[number]))
            else:
                print(shift_left(string_input_list[number]))
        except IndexError:
            pass

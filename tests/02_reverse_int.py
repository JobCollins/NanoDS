def reverse_int(num):
    
    reversed_num = 0
    while num > 0:
        remainder = num%10
        reversed_num = (reversed_num*10)+remainder
        num = num//10
    while num < 0:
        remainder = abs(num)%10
        print(remainder)
        reversed_num = (reversed_num*10)+remainder
        num = num//10
    return reversed_num


print(reverse_int(-120))
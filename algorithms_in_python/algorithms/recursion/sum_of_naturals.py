

def sum_nums(num):
    
    if num == 0:
        return 0
    
    return sum_nums(num-1) + num


t = sum_nums(6)
print(t)
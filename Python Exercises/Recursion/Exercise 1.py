# sum of list

def list_sum(list):
    sum = 0
    for val in list:
        sum = val + sum
    return sum

print(list_sum([2,4,5,6,7]))
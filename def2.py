def average(*args):
    num = 0 
    for num_2 in args:
        num += num_2
    
    return num / len(args)


print(average(12, 16, 18 ))
def find_outlier(integers1):
    only_odd = [num for num in integers1 if num % 2 == 1]
    only_even=[num for num in integers1 if num%2!=1]
    if len(only_odd)==1:
        return only_odd[0]
    else:
        return only_even[0]



print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))

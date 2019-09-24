#You are given an array (which will have a length of at least 3, but could be very large) containing integers.
# The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N.
# Write a method that takes the array as an argument and returns this "outlier" N.
#Examples
#[2, 4, 0, 100, 4, 11, 2602, 36]
#Should return: 11 (the only odd number)

#[160, 3, 1719, 19, 11, 13, -21]
#Should return: 160 (the only even number)

def find_outlier(integers1):
    only_odd = [num for num in integers1 if num % 2 == 1]
    only_even=[num for num in integers1 if num%2!=1]
    if len(only_odd)==1:
        return only_odd[0]
    else:
        return only_even[0]



print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))

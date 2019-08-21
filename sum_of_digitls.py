#A digital root is the recursive sum of all the digits in a number. Given n, take the sum of the digits of n.
# If that value has more than one digit, continue reducing in this way until a single-digit number is produced.
# This is only applicable to the natural numbers.
# Here's how it works:
# digital_root(942)
# => 9 + 4 + 2
# => 15 ...
# => 1 + 5
# => 6

def digital_root(a):
    s=0
    for i in str(a):
        s+=int(i)
    if s<10:
        return s
    else:
        return digital_root(s)


print(digital_root(6))
#Write a function that takes an integer as input,
# and returns the number of bits that are equal to one in the binary representation of that number.
# You can guarantee that input is non-negative.
#Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
def countBits(n):
    digit2=0

    for digit1 in bin(n)[2:]:
        if digit1=='1':
            digit2+=1

    return digit2

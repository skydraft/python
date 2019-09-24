#You are given an input string.
#For each symbol in the string if it's the first character occurence, replace it with a '1', else replace it with the amount of times you've already seen it...
#But will your code be performant enough?

#Examples:
#input   =  "Hello, World!"
#result  =  "1112111121311"

#input   =  "aaaaaaaaaaaa"
#result  =  "123456789101112"

def numericals(s):

    st = ''
    dic = {}

    for i in s:
        if i in dic:

            dic.update({i: dic.get(i)+1})
            st+=str(dic.get(i))
        else:
            dic.update({i:1})
            st += '1'


    return st




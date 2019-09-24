def numericals(s):

    st = ''
    count=0

    for i in s:
        count+=1
        t=s[:count].count(i)
        st+=str(t)


    return st




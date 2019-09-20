def numericals(s):

    sum1=1

    st='1'
    s1=s[0]

    print()
    for i in s[1:]:
        for j in s1:
            if j==i:
                sum1+=1
        if sum1==1:
            st +='1'
        else:
            st += str(sum1)
            sum1=1
        s1+=i

    return st

#__________________________________________

def numericals1(s):

    sum1=1

    st='1'
    s1=s[0]
    d=dict.fromkeys(s)

    for i in s[1:]:
        for j in s1:
            if j==i:
                sum1+=1
        if sum1==1:
            st +='1'
        else:
            st += str(sum1)
            sum1=1
        s1+=i

    return st
#print(numericals("à¼ÅÑã9LxÏ±{çµ*±wzN½«Èp¯ÛEØ@!¨ ·L~rË9fOf«&GPS¢­"))
#11111111111111121111111111111111121111211221111211111
print(numericals1("hello"))



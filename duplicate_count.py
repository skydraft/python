def duplicate_count(text):

    a=[]
    dub=0
    for i in text.lower():
        s=0
        p=0

        for j in text.lower():

            if j==i:
                s+=1

                if s>1:
                    for k in a:

                      if k==j:
                         p+=1
                    if p==0:
                       a.append(i)

    return len(a)


print(duplicate_count("aA11"))

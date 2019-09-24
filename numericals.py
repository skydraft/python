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




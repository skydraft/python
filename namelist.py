def namelist(names):
    st1=''

    count=0
    for i in names:

        if len(names)==1:
            st1 = st1 + i.get('name')
            break

        if count==len(names):
            st1 = st1 +i.get('name')

        if count==len(names)-1:
            st1 = st1+" & "+i.get('name')
            break
        else:
            st1=st1+" "+i.get('name')
        count += 1
        if count<len(names)-1:
            st1+=","





    return st1.lstrip()


print(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'}]))
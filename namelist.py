def namelist(names):
    st1=''
    if len(names)==0:
        return ''
    if len(names)>1:
        for i in names[:-1]:
            st1 += i.get('name') + ", "
        st1=st1[:-2]+" & "+ names[-1].get('name')
        return st1
    else:
        st1 += names[-1].get('name')
        return st1



print(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'}]))
#Given: an array containing hashes of names
#Return: a string formatted as a list of names separated by commas except for the last two names,
# which should be separated by an ampersand.
#Example:
#namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'
#namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'
#namelist([ {'name': 'Bart'} ])
# returns 'Bart'
#namelist([])
# returns ''



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
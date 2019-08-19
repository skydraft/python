#сумма многочленов/sum of polynomials
#input:
#a: 6x+11
#b:1x^5+2x^4+3x^3+5x^2+2x+1
#output:[1, 2, 3, 5, 8, 12]
# 1x^5+2x^4+3x^3+5x^2+8x+12


a=[6,11]
b=[1, 2 ,3,5,2,1]
c=[]
if len(a)>=len(b):
    m = len(a) - len(b)
    for i in range(m):
        b=[0]+b

    for i in range(0,len(a),1):
        c.append(a[i]+b[i])

else:
    m=len(b)-len(a)
    for i in range(m):
        a=[0]+a

    for i in range(0,len(b),1):

        c.append(b[i]+a[i])

print(c)

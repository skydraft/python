#сумма многочленов/sum of polynomials
#input:
#a: 6x+11
#b:1x^5+2x^4+3x^3+5x^2+2x+1
#output:[1, 2, 3, 5, 8, 12]
# 1x^5+2x^4+3x^3+5x^2+8x+12

c1=int(input())
c=input()
a= [int(k) for k in c.split()]
c2=input()
c=input()
b= [int(k) for k in c.split()]
z=[]
if len(a)>=len(b):

    m = len(a) - len(b)
    print(c1)
    for i in range(m):
        b=[0]+b


    for i in range(0,len(a),1):
        z.append(a[i]+b[i])

else:
    m=len(b)-len(a)
    print(c2)
    for i in range(m):
        a=[0]+a

    for i in range(0,len(b),1):

        z.append(b[i]+a[i])

print(*z)


def NRecurssion(n):
    if n>100:
        return n-10
    elif n<=100:
        return NRecurssion(NRecurssion(n+11))

n=int(input('Enter a number: '))
res=NRecurssion(n)
print(res)
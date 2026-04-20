s=input('Enter your name: ')
mid=len(s)//2
first=s[:mid]
seconf=s[mid:]
frev=first[::-1]
srev=seconf[::-1]
res=frev+srev
print(res)
marks=int(input('Enter Marks: '))
if marks>=90 and marks<=100:
    print('Grade A+')
    print('Distinction')
elif marks>=80 and marks<=89:
    print('Grade A')
    print('Distinction')
elif marks>=70 and marks<=79:
    print('Grade B')
    print('Pass')
elif marks>=60 and marks<=69:
    print('Grade C')
    print('Pass')
elif marks>=50 and marks<=59:
    print('Grade D')    
    print('Pass')
else:
    print('Grade F')
    print("Fail")


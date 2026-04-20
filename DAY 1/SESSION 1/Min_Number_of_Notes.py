amount=int(input('Enter change amount: '))
notes=[100,50,20,10,2,1]
print('Minimum Notes required')
for note in notes:
    count=amount//note
    if count>0:
        print(note,":",count)
        amount=amount%note
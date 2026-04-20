current_balance = int(input("Enter your balance: "))
SavingsAccount = input('Enter account type (1 For Savings, 2 For Current): ')
WithDraw=int(input("Enter amount to be withdrawn: "))

if WithDraw<current_balance:
    if SavingsAccount ==1:
        if WithDraw>50000:
            print('EXCEEDS MAXIMUM LIMIT')
        else:
            if WithDraw%100==0:
                current_balance-=WithDraw
            else:
                print('Not a multiple of 100')
            if current_balance <=500:
                print("INSUFFICEINT BALANCE")
            else:
                print('1 Savings')
                print('SUCCESS')
                print('Current Balance: ',current_balance)
    else:
        if SavingsAccount==2:
            
            if WithDraw>25000:
                current_balance-=50
                print('2 Current')
                print('Withdrawn Amount: ',WithDraw)
                print('Current Balance: ',current_balance)
                
            

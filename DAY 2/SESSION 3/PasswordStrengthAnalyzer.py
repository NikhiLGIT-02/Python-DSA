def password_checker(n):
    score=0

    if has_min_length(n):
        score+=1
    if has_uppercase(n):
        score+=1
    if has_lowercase(n):
        score+=1
    if has_special_charecter(n):
        score+=1
    print('Score: ',score)

    if score==4:
        print('Strong')
    elif score>=2:
        print('Moderate')
    else:
        print('Weak')

def has_min_length(n):
    return len(n)>=8

def has_uppercase(n):
    return any(char.isupper() for char in n)


def has_lowercase(n):
    return any(char.islower() for char in n)

def has_special_charecter(n):
    special_char = '!@#$%^&*'
    return any(char in special_char for char in n)


n=input("Enter your Password: ")
password_checker(n)
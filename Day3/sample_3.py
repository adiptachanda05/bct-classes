# write a python program for check the input age is kidss,child,teen or adults 

age = int(input('Enter your age: '))
if age >= 0 and age <= 5:
    print('You are a KID')
elif age >= 6 and age <= 12:
    print('You are a CHILD')
elif age >= 13 and age <= 19:
    print('You are a TEEN')
elif age >= 20:
    print('You are an ADULT')
else:
    print('Invalid age entered!')

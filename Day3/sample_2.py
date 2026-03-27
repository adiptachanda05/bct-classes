# write a python program to check ages for eligible voter and the age will be user inputed

age = int(input('Enter your age: '))

if age >= 18:
    print('You are eligible to vote!')
else:
    print('You are not eligible to vote yet. Please wait', 18 - age, 'more years.')
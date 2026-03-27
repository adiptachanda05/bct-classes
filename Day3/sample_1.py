
#write a python programe for swapping of two numbers without using temp or 3rd variable

a= int(input('Enter 1st number'))
b= int(input('Enter 2nd number'))

print('before swapping : a=',a, 'b=',b)
a = a + b
b = a - b
a = a - b
print('after swapping : a=',a, 'b=',b)
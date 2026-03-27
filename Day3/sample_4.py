# write a python program to sum of 1st 10 natural numbers

n = int(input('Enter number of terms:'))
sum = 0
for i in range(1, n + 1):
    sum += i
print('Sum of first', n, 'natural numbers =', sum )

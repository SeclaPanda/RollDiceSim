import random

def roll(num1, num2):
    return random.randint(num1, num2)

print('Welcome to dice rolling simulator')

while True:
    print('How many side u want: (a)1-6 or (b)1-24 or may be (c)specific?')
    print('To exit print - exit')
    a = input().lower()
    if a == 'exit':
        break
    if a == 'a':
        b = roll(1, 6)
    if a == 'b':
        b = roll(1, 24)
    if a == 'c':
        num1 = int(input('Enter start point: '))
        num2 = int(input('Enter end point: '))
        b = roll(num1, num2)
    print(b, '\n')
print('Program ended')

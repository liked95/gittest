from unicodedata import name
from cs50 import get_string


print('How is your day?')
print('How is your day')

print(3+2-100)

print(3**3)

# I want the result of 3 powered by 3[]

# sorry I want a new func
print('Something unusual happens')

# Command line argument

def say():
    name = input('What is your name: ')
    print('Hello, ' + name)

def giaithua(x):
    if x == 1:
        return 1
    return x*giaithua(x-1)

print(giaithua(5*10))




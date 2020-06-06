"""
For the numbers 1 to 100.
If the number is divisible by 3 print out the word Fizz.
else if the number is divisible by 5 print out the word Buzz.
else if the number is divisible by 3 and 5 print out the word FizzBuzz.
Else print out the number
"""
# Counter from 1 to 101(exclusive)
n: int
for n in range(1, 101):
    if n % 5 and n % 3:
        print("FizzBuzz")
    elif n % 3:
        print("Fizz")
    elif n % 5:
        print("Buzz")
    else:
        print(n)

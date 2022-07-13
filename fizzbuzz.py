lst = []
n = int(input("Enter your number: "))
for i in range(1,n+1):
    if i%5 == 0 and i%3 == 0:
        i = "Fizzbuzz"
    elif i%5 == 0:
        i = 'Buzz'
    elif i%3 ==0:
        i = 'Fizz'
    lst.append(i)
print(lst) 

""" Problem description: Given an integer n, return a string array result where:

result[i] == “FizzBuzz” if i is divisible by 3 and 5.
result[i] == “Fizz” if i is divisible by 3.
result[i] == “Buzz” if i is divisible by 5.
result[i] == i in any other case.
You should check for the FizzBuzz condition first, as it checks for multiple conditions.
 For example, the number 15 is divisible with both 3 and 5, so FizzBuzz should get printed. 
 15 is also divisible by 3 and 5 individually, and we don’t want Fizz or Buzz printed alone."""
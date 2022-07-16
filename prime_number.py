def isprime(n):
    if  n == 0 or n==1: #checks if the value is 0 or 1 to qualify for prime number comparison
        print("not a prime")
    else:               #if value is greater than 1 than this conditon followed by loop executes.
        for i in range(2,n): #starting from 2 till second last number since the number can be divisble by itself(prime number rule).
            if (n % i == 0): 
                print(n,"is not a prime number but a composite number.")
                break     #if the above condition qualifies the program breaks and prints the statement.
        else:
            print(n,"is a prime number.")
            
    return True
    
num = int(input("Enter your number: ")) #input by user
isprime(num)                            #function call





num = int(input('Enter your number: '))  
a ,total = 0,0 #initilization
b = 1
fib_list = [] #empty list
for i in range(num): #loop 
    total +=a 				#increment by a
    fib_list.append(total)  #adds the value to the list
    a = b
    b = total
print(fib_list)             #prints the list once the loop is completed

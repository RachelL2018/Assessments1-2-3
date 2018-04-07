#Rachel Leonard 
#Collatz Conjecture
n= int(input("enter number: "))#defines varible n of type interger which takes an input from user
while n != 1: #loops while n not equal to 1
    if n % 2 == 0: #defines a condition if n is even
        n= n/2 #It will divide n by 2 and store the new value in the varaible n
        print(n)# and print the new value in n
    else:  # if n not even
        n=(n*3)+1#it will multiple n by 3 and add 1 and store the new value in the varaible n
        print(n)# and it will print this new value in n
        
        

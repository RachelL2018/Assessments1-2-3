#Rachel Leonard/Euler problem 5 solution

#defines a function that the parameter num is passed to
def divisable(num):
#for loop which loops 20 times. It also loops through 1 to 20 assigning i a value which increments each time it loops 
    for i in range(1,21):
        if num % i != 0:# it divides the varaible num by i each time it loops.
                           #It also states a condition that if each time num is divided by i it is not even it returns a boolean of false
            return False
    return True

num = 1 # defines a varaible called num and sets it to 1
while True: #while loop which loops until true
    if divisable(num): #calls the function divisable and stops if True is returned from the function
        break
    num += 1 #sets the varaible to increment each time it loops

print(num)# prints the value stored in num.


        




#Rachel Leonard/Euler problem 5 solution

#create a function that takes in argument num
def divisable(num):
#for loop which loops through 1 to 20
    for i in range(1,21):
        if num % i != 0:# it divides the varaible num by i each time it loops.It also states a condition that if each time num is divided by i it is not even it returns a boolean of false
            return False
    return True
#defines a varaible called num and sets it 1
num = 1#while loop which loops until True
while True:
    if divisable(num): #calls the function divisable and stops when True
        break
    num += 1 #the varaible increments each time it loops

print(num)# prints the number 


        

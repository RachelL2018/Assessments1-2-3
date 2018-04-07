
#Rachel Leonard week 6

def factorial(num):#defines a function 

   sum = num #create varaible sum and set the value to the number taken in from input varaible num
   for i in range(1, num):# loop the number of times less 1 of the value stored in num.
        sum = sum * i #sum which currently stores the value input by user is multipled by i which begins at 1 
                       #and increments by 1 each time it loops.
                       #Each time it loops the new value is stored in sum and this value is then taken into the calculation.
            
   return sum # when loop is finished return that value stored in num


print("The factorial is:",factorial(num= int(input("Enter first number:"))))# the function is called and input taken in and passed 
                                                                             #as a parameter to it. The result is then printed.








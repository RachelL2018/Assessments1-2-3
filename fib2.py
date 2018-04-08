#Rachel Leonard
# A program that displays Fibonacci numbers using people's names.

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

name = input("enter your surname  ") # creates a variable which takes in a string from the user
first = name[0] # creates a varaible which gets the first character from the varaible name and stores it
last = name[-1] # creates a varaible which gets the last character from the varaible name and stores it
firstno = ord(first)#creates a varaible which stores the value of the integer that represents the unicode point of the character stored in firstno using ord fucntion to obtian is 
lastno = ord(last)#creates a varaible which stores the value of the integer that represents the unicode of the character stored in lastno using ord function to obtain it
x = firstno + lastno#creates a varaible which stores that value of the sum of the tow variables firstno and lastno

ans = fib(x)# creates a variable which stores the result of the called function fib which passed the parameter x to it
print("My surname is", name)
print("The first letter", first, "is number", firstno)
print("The last letter", last, "is number", lastno)
print("Fibonacci number", x, "is", ans)# prints  a string and the value of the varibke x and the value of the ans which contains the result of the called function.

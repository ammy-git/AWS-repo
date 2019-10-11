    # Store input numbers
    num1 = input('Enter first number: ')
    num2 = input('Enter second number: ')
    # Add two numbers
    sum = float(num1) + float(num2)
    # Display the sum
    print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))
#i m editing new code
# Python Program to find the L.C.M. of two input number

# define a function
def lcm(x, y):
   """This function takes two
   integers and returns the L.C.M."""

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm
#i m again editing python file
# Python program to find the L.C.M. of two input number

# define gcd function
def gcd(x, y):
   """This function implements the Euclidian algorithm
   to find G.C.D. of two numbers"""

   while(y):
       x, y = y, x % y

   return x


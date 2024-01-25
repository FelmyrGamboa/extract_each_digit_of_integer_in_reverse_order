# Exercise 11: Write a Program to extract each digit from an integer in the reverse order.
# For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.

#Create a variable containing the integer
given_number = 7536

#Create a loop with a certain condition to stop
while given_number != 0:
#Reverse the digits of integer by dividing it by 10 and getting the remainder
    reverse_digit = given_number % 10
#Assign the quotient as the new integer to be divided
    given_number //= 10
#Display the result with spaces 


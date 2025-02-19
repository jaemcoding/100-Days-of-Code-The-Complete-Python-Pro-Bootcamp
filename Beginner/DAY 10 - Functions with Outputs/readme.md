# 1. Leap Year
💪 This is a difficult challenge! 💪 

Write a program that returns True or False whether if a given year is a leap year.

A normal year has 365 days, leap years have 366, with an extra day in February. The reason why we have leap years is really fascinating, this video does it more justice



This is how you work out whether if a particular year is a leap year. 

- on every year that is divisible by 4 with no remainder

- except every year that is evenly divisible by 100 with no remainder 

- unless the year is also divisible by 400 with no remainder   



If English is not your first language, or if the above logic is confusing, try using this flow chart.



e.g. The year 2000: 

2000 ÷ 4 = 500 (Leap)  
2000 ÷ 100 = 20 (Not Leap)  
2000 ÷ 400 = 5 (Leap!)  
So the year 2000 is a leap year. 



But the year 2100 is not a leap year because: 

2100 ÷ 4 = 525 (Leap)  
2100 ÷ 100 = 21 (Not Leap)  
2100 ÷ 400 = 5.25 (Not Leap)  


Warning

Your return should be a boolean and match the Example Output format exactly, including spelling and punctuation. 



Example Input 1

2400

Example Return 1

True



Example Input 2

1989

Example Return 2

False





How to test your code and see your output?



Udemy coding exercises do not have a console, so you cannot use the input() function. You will need to call your function with hard-coded values like so:



def is_leap_year(year):
  # your code here
 
# Call your function with hard coded values
is_leap_year(2024)


# 2. Calculator Project
The goal is to build a calculator program.

Demo
https://appbrewery.github.io/python-day10-demo/

Storing Functions as a Variable Value
You can store a reference to a function as a value to a variable. e.g.

def add(n1, n2):
    return n1 + n2
    
    
my_favourite_calculation = add
my_favourite_calculation(3, 5)  # Will return 8
In the starting file, you'll see a dictionary that references each of the mathematical calculations that can be performed by our calculator. Try it out and see if you can get it to perform addition, subtraction, multiplication and division.

PAUSE 1
TODO: Write out the other 3 functions - subtract, multiply and divide.

PAUSE 2
TODO: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"

PAUSE 3
TODO: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary.

Functionality
Program asks the user to type the first number.
Program asks the user to type a mathematical operator (a choice of "+", "-", "*" or "/")
Program asks the user to type the second number.
Program works out the result based on the chosen mathematical operator.
Program asks if the user wants to continue working with the previous result.
If yes, program loops to use the previous result as the first number and then repeats the calculation process.
If no, program asks the user for the fist number again and wipes all memory of previous calculations.
Add the logo from art.py
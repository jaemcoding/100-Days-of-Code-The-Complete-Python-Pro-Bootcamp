# 1. Grading Program
You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the names of the students and the values are their exam scores. 



Write a program that converts their scores to grades.



By the end of your program, you should have a new dictionary called student_grades that should contain student names as keys and their assessed grades for values. 



The final version of the student_grades dictionary will be checked. 



**DO NOT** modify lines 1-7 to change the existing student_scores dictionary. 



This is the scoring criteria: 

- Scores 91 - 100: Grade = "Outstanding" 

- Scores 81 - 90: Grade = "Exceeds Expectations" 

- Scores 71 - 80: Grade = "Acceptable" 

- Scores 70 or lower: Grade = "Fail" 

# 2. Blind Auction Project
The goal is to build a blind auction program.

Demo
https://appbrewery.github.io/python-day9-demo/

Clearing the Output
There are several ways of clearing the output. The easiest is to simply print "\n" many times so that the output scrolls down many lines.

e.g.

# This will add 20 new lines to the output
print("\n" * 20)
Functionality
Each person writes their name and bid.
The program asks if there are others who need to bid. If so, then the computer clears the output (prints several blank lines) then loops back to asking name and bid.
Each person's name and bid are saved to a dictionary.
Once all participants have placed their bid, the program works out who has the highest bid and prints it.
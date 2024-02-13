# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = weight / (height ** 2)
if BMI >= 35:
  print("Your BMI is " + str(BMI) + ", you are clinically obese.")
elif 30 <= BMI < 35:
  print("Your BMI is " + str(BMI) + ", you are obese.")
elif 25 <= BMI < 30:
  print("Your BMI is " + str(BMI) + ", you are slightly overweight.")
elif 18.5 < BMI < 25:
  print("Your BMI is " + str(BMI) + ", you have a normal weight.")
else:
  print("Your BMI is " + str(BMI) + ", you are underweight.")

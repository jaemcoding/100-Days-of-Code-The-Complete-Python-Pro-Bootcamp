# # """Write your code below this line 👇
# def prime_checker(number):
#     if number % 2 == 0:
#         print("It's not a prime number.")
#     elif number % 3 == 0:
#         print("It's not a prime number.")
#     else:
#         print("It's a prime number.")
#
# # Write your code above this line 👆
#
# # Do NOT change any of the code below👇
# n = int(input())  # Check this number
# prime_checker(number=n)
def prime_checker(number):
  is_prime = True
  for i in range(2, number):
    if number % i == 0:
      is_prime = False
  if is_prime:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")
# Your code above this line 👆
n = int(input()) # Check this number
prime_checker(number=n)
def calculate_factorial(n):
  #Calculating the factorial of a given number n 
  factorial = 1
  while n > 1:
    factorial *= n
    n -= 1
  return factorial

while True: #Prompting a user for their input 
  user_input = input("Enter a non-negtive integer to calculate it's factorial (or 'q' to quit) : ")

  if user_input.lower() == 'q':
    print("Exiting the program. Goodbye!")
    break
  try: #Validating input from a user and converting a input to integer
  number = int(user_input)
  if number < 0:
    print("Please enter a non-negative integer.")
  else:
    result = calculate_factorial(number)
    print(f"The factorial of {number} is {result}. ") #displaying the factorial result 
except ValueError:
  print ("Invalid input. Please enter a non-negative integer.")
         

#Promoting the user to input the height of the pyramid 
height = int (input("Enter the height of the pyramid: "))

for i in range (1, height + 1): #using a for loop to iterate through the range of 1 to the user's inputted height 
  print (" " * (height - i) + "*" * (2 * i - 1)) #printing spaces multiplied by height-i to create a left-side alginment, followed by asterisks multipled by (2 * i - 1)

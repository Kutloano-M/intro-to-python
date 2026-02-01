#These are predfined credentials
valid_username = "Kutloano1"
valid_password = "401223709"

#Prompting the user for their username and password 
input_username = input ("Enter your username please: ")
input_password = input ("Enter your password please: ")

#Validating the credentials to verify if username and password are the same 
if input_username == valid_username and input_password == valid_password:
  print ("Authentication successful ! Welcome ", valid_username)
else:
  if input_username != valid_username:
    print ("Invalid username.")
  if input_password != valid_password:
    print ("Invalid password. ")

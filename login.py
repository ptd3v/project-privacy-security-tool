username="Username"
password="Password"

inputuser=input('[*] Enter Your Username: ')
inputpass=input('[*] Enter Your Password: ')

if not (username==inputuser and password==inputpass):
    print('Incorrect Username or pAssword! Please try again.')
    exit() #Built in Function

print("This is the correct Passwordn")

#I need to come back to this after some sleep, it's a lot more complex than I assumed.

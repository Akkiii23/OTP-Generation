import random
otp = random.randint(100000,999999)
print("Enter the OTP which get on your register mobile number:",otp)
user = int(input("Enter the six digit OPT:"))
if otp == user:
    print("Welcome to Home")
else:
    print("Please enter the correct OPT")

# Do not edit any of the starte code. Use the comments as a guide to complete the assignment.

print ("Welcome to the rollercoaster")

# Step 1:Ask the user about their height. 
height = int(input("What is your height in inches? "))

# Step 2: Ask for their age.
age = int(input("What is your age? "))

#Step 3: Create an if statement that matches for their responses. You may need multiple if/elif statements. 
    # Use the logic flow diagram to help you
if height >=60:
    print("You can ride? ")
    if age<12:
        print("Please pay $5. ")
        bill = 5
    elif age <=18:
       print("please pay $7 ")
       bill=7
    else:
        print("Please pay $12.")
        bill= 12
    print("Photos are $3 extra")
    photo=input("Do you want a photo? ")
    if photo=="yes":
        bill = bill+3
        bill=str(bill)
        print("Your final bill$"+bill+".")
    else :
        bill=str(bill)
        print("your total is $"+bill+".")
else:
 print("Sorry you cant ride")
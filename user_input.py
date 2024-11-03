#Function to print customize user input
def userInput(name, age, location):
    return f"Your Name is: {name}, Your Age is: {age} and Your Location is:  {location}"


name = input("Enter Your Name: ")
age = input("Enter Your Age: ")
location = input("Enter Your Location: ")

print(userInput(name, age, location))

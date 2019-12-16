
# Declare a variable called `name`, and store your name inside it.
name = "Peleke"

# Print the message: "My name is <YOUR NAME HERE>"
print("My name is " + name + ".")

# Declare a variable called `age`, and store your age inside it.
age = 42
# Reminder: int type is a whole number, positive or negative.
age = -42

# Print the message: "I am <YOUR AGE HERE> years old."
print("I am " + str(age) + " years old.")

#######################################################
# Declare a variable called `pizza_price`, and store a number inside it.
pizza_price = 12

# Declare a variable called `number_of_pizzas`, and store a number inside it.
number_of_pizzas = 4

# Store the total price for all the pizzas in a variable called `total_price_of_pizzas`.
total_price = number_of_pizzas * pizza_price

# Print the message: "The price of a single pizza is $<PRICE OF PIZZA>."
print("The price of a single pizza is $" + str(pizza_price) + ".")

# Print the message: "We are buying <NUMBER OF PIZZAS> pizzas."
print("We are buying " + str(number_of_pizzas) + " pizzas.")

# Print the message: "The total price for all the pizzas is <TOTAL PRICE OF PIZZAS>."
print("The total price of pizza is $" + str(total_price) + ".")

#######################################################
# Create a list called `favorite_countries`. Store the name of four favorite countries inside it.
favorite_countries = ["Norway", "Spain", "Taiwan", "Morocco"]

# Print the message: "My favorite countries are: <YOUR LIST HERE>."
print("My favorite countries are: " + str(favorite_countries) + ".")

#######################################################
# Create a dictionary called `contact_information` and store a home phone number, a cellphone number, and an email address inside of it.
contact_information = {
  "email": "BoBoTheClown@gmail.com",
  "cell_number": "203-976-0988",
  "home_phone": "203-867-5309"
} 

# Print out the message: "Please contact me at <EMAIL> or call me at <HOME PHONE>"
print("Please contact me at " + contact_information["email"] + " or call me at " + contact_information["home_phone"])

# Print out the message: "In case of an emergency call <CELL NUMBER>"
print("In case of an emergency, call " + contact_information["cell_number"])


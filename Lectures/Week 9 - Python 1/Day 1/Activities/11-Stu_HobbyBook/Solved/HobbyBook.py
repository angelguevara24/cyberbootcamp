# Dictionary full of info
my_info = {"name": "Rex",
           "occupation": "dog",
           "age": 21,
           "hobbies": ["barking", "eating", "sleeping", "loving my owner"],
           "wake-up": {"Mon": 5, "Friday": 5, "Saturday": 10, "Sunday": 9}}

# Print out results are stored in the dictionary
print("Hello I am " + my_info["name"] + " and I am a " + my_info["occupation"])
print("I have " + str(len(my_info["hobbies"])) + " hobbies!")
print("On the weekend I get up at " + str(my_info["wake-up"]["Saturday"]))
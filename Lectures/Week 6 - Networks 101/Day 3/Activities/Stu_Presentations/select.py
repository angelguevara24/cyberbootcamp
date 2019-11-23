import random

with open("protocols", "r") as file:
    protocols = file.read().splitlines()
    targets = random.sample(protocols, 2)
    print(f"Your protocols are: `{targets[0]}` and `{targets[1]}`.")

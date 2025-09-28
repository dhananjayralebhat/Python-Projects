import random

subjects = [
    "Mahendra Singh Dhoni",
    "Virat Kohli",
    "A Mumbai Cat",
    "A Group of Monkeys",
    "Auto Rickshaw Driver",
    "Hardik Pandya"
]

actions = [
    "launches",
    "cancels",
    "dances with",
    "eats",
    "declares war on"
    "orders",
    "celebrates"
]

places_of_things = [
    "at Red Fort",
    "In Local Train",
    "Plate of Samosa",
    "Inside city",
    "At Ghat"
    "during IPL match"
]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    places_of_thing = random.choice(places_of_things)

    headline = f"BREAKING NEWS: {subject} {action} {places_of_thing}"
    print("\n"+headline)

    user_input = input("\nDo you want another headline? (yes/no)").strip().lower()

    if user_input=="no":
        break

        print("\nThanks for using Fake Headline Generator. Have a fun day")

attendees = ["Ken", "Alena", "Treasure"]
attendees.append("Ashley")
attendees.extend(["James", "Gull"])
optional_invitees = ["Ben J.", "Dave"]
potential_attendees = attendees + optional_invitees
print("There are", len(potential_attendees), "potential attendees currently")

books = [
    "Learning Python: Powerful Object-Oriented Programming - Mark Lutz",
    "Automate the Boring Stuff with Python: Practical Programming for Total Beginners - Al Sweigart",
    "Python for Data Analysis - Wes McKinney",
    "Fluent Python: Clear, Concise, and Effective Programming - Luciano Ramalho",
    "Python for Kids: A Playful Introduction To Programming - Jason R. Briggs",
    "Hello Web App: Learn How to Build a Web App - Tracy Osborn",
]

print("Suggested gift: {}".format(books[0])
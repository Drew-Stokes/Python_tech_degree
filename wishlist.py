books = [
    "Learning Python: Powerful Object-Oriented Programming - Mark Lutz",
    "Automate the Boring Stuff with Python: Practical Programming for Total Beginners - Al Sweigart",
    "Python for Data Analysis - Wes McKinney",
    "Fluent Python: Clear, Concise, and Effective Programming - Luciano Ramalho",
    "Python for Kids: A Playful Introduction To Programming - Jason R. Briggs",
    "Hello Web App: Learn How to Build a Web App - Tracy Osborn",
]

print("Suggested gift: {}".format(books[0])

print("Books:")
for book in books:
    print("* " + book)
    
def display_wishlist(display_name, wishes):
  items = wishes.copy()
  print(display_name + ":")
  suggested_gift = items.pop(0)
  print("======>", suggested_gift, "<======")
  for item in items:
    print("* " + item)
  print()
  
display_wishlist("Books", books)
display_wishlist("Video Games", video_games)
      
continents = [
    'Asia',
    'South America',
    'North America',
    'Africa',
    'Europe',
    'Antarctica',
    'Australia',
]
# Your code here
for continent in continents:
    if continent[0] == "A":
        print(f"* {continent}")

all_restaurants = [
    "Taco City",
    "Burgertown",
    "Tacovilla",
    "Hotdog station",
    "House of tacos",
]

def tacos_only(restaurants):
    taco_joints = restaurants.copy()
    for taco_joint in taco_joints.copy():
        if "taco" not in taco_joint.lower():
            taco_joints.remove(taco_joint)
    return taco_joints

dinner_options = tacos_only(all_restaurants)

turtles = [
    "Michelangelo",
    "Leonardo",
    "Raphael",
    "Donatello",
]

def shredder(names):
    if len(names) >= 1:
        names[0] = "Bebop"

shredder(turtles)

for turtle in turtles:
    print("* " + turtle)


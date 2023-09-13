class Dog:
  # To create a Dog, give it a name, breed, and age. age is in years. 
  # If you don't give an age, we'll say it's 0 years old (a puppy).
  # All dogs also start as friendly!
  def __init__(self, input_name, input_breed, input_age = 0, input_friendliness = True):
    # self.name is this specific dog's name
    self.name = input_name
    self.breed = input_breed
    self.age = input_age
    self.is_friendly = input_friendliness
    self.friends = []

      # The self parameter refers to the specific
  # dog we're attaching this method to.
  def have_birthday(self):
    #  Add one to this specific dog's age.
    self.age = self.age + 1
    # Print out the change we made.
    print("{name} had a birthday! {name} is {age} years old.".format(name = self.name, age = self.age))

     # self will equal this specific dog
  # other_dog will be an argument we pass in
  def become_friends(self, other_dog):
    if(other_dog.is_friendly):
      # If the other dog is friendly,
      # it adds other_dog to its friends
      self.friends.append(other_dog)
      # The other dog also adds this 
      # specific dog to its friends
      other_dog.friends.append(self)
      print("{name} become friends with {other_name}!".format(name = self.name, other_name = other_dog.name))
    else:
      # If the other dog is NOT friendly,
      # no one becomes friends.
      print("{other_name} did not want to become friends with {name}!".format(name = self.name, other_name = other_dog.name))

   
  def __repr__(self):
    # Printing a Dog will tell you its name, its breed, its age, if it's friendly, and how many friends it has.
    description = "This {breed} named {name} is {age} years old and has {number_of_friends} friends.".format(breed = self.breed, name = self.name, age=self.age, number_of_friends=len(self.friends))
    if self.is_friendly:
      description += " {name} is a friendly dog.".format(name = self.name)
    else:
      description += " {name} is an unfriendly dog.".format(name = self.name)
    return description

dog_one = Dog("Sparky", "Golden Retriever", 5)
# This dog will have self.is_friendly set to False
dog_two = Dog("Bruno", "Chihuahua", 10, False)


# The self parameter will see that self = dog_one
dog_one.have_birthday()
# Output: "Sparky had a birthday! Sparky is 6 years old."

'''
Next, we’ll revisit our two _instance_s of our Dog class. In this example, we need two Dogs so they can become friends! First, let’s see if “Sparky”, who is friendly, can become friends with “Bruno” who is NOT friendly.
'''

# When Sparky asks Bruno, Bruno says no.
dog_one.become_friends(dog_two)
# Output: "Bruno did not want to become friends with Sparky!"

'''
Since “Bruno” is not friendly, Bruno doesn’t want to be friends! But wait, what if Bruno initiates the friendship? If Bruno asks Sparky, Sparky will accept the friendship because Sparky IS friendly.
'''

# When Bruno asks Sparky, Sparky says yes!
dog_two.become_friends(dog_one)
# Output: "Bruno became friends with Sparky!"
print(dog_one)
##########################################################


# You can start with the
# Cat class or erase this
# and use your own!
class Cat:
  # Create a __init__ method
  def __init__(self, input_name, input_age, input_color, input_purr=False, input_mouser=False):
    self.name = input_name
    self.age = input_age
    self.color = input_color
    self.does_purr = input_purr
    self.is_mouser = input_mouser
    self.hunting_buddies = []

  def __repr__(self):
    description = "This {color} cat named {name} is {age} years old and has {num_of_hunting_buddies} hunting buddies.".format(color=self.color, name=self.name, age=self.age, num_of_hunting_buddies=len(self.hunting_buddies))
    
    if self.is_mouser:
      description += " {name} is a mouse hunter.".format(name=self.name)
    else:
      description += " {name} is not a mouse hunter.".format(name=self.name)
    
    if self.does_purr:
      description += " {name} is known for purring.".format(name=self.name) 
    else:
      description += " {name} is not known for purring.".format(name=self.name) 
    return description  

# Create a new pet!
  # Create method to change
  # at least one attribute.
  # Ex: def change_att(self):
  def have_birthday(self):
    self.age = self.age + 1
    print("{name} had a birthday! {name} is now {age} years old!!".format(name = self.name, age = self.age))

#Create method where two
  # pets interact.
  # Ex: def name(self, pet):
  def become_hunting_buddies(self,other_cat):
    if(other_cat.is_mouser):
      self.hunting_buddies.append(other_cat)
      other_cat.hunting_buddies.append(self)

      print("{name} became hunting buddies with {other_cat}!".format(name = self.name, other_cat = other_cat.name))
    else:
        print("{other_cat} did not want to be friends with {name}".format(name = self.name, other_cat = other_cat.name))

  



# Create your new pet.
cat_one = Cat("Thor", 8, "Black", True, False)
# Create second/third pet.
cat_two = Cat("Leo", 3, "Tabby", False, True)
cat_three = Cat("Lion-O", 5, "White", True, True)

# Call your method on your
# new pet here.

cat_one.have_birthday()
cat_two.become_hunting_buddies(cat_one)

print(cat_one)
print(cat_two)
print(cat_three)


########################################################

'''
You go to measure several circles you happen to find around.

A medium pizza that is 12 inches across.
Your teaching table which is 36 inches across.
The Round Room auditorium, which is 11,460 inches across.
You save the areas of these three things into pizza_area, teaching_table_area, and round_room_area.

Remember that the .radius of a circle is half the diameter. We gave three diameters here, so halve them before you calculate the given circle’s area.
'''

class Circle:
  pi = 3.14
  def area(self, radius):
    return self.pi * (radius**2)

circle = Circle()

pizza_area = circle.area(12 / 2)
print(pizza_area)

teaching_table_area = circle.area(36 / 2)
print(teaching_table_area)

round_room_area = circle.area(11460 / 2)
print(round_room_area)

###################################################

class Shouter:
  def __init__(self, phrase):
    # make sure phrase is a string
    if type(phrase) == str:

      # then shout it out
      print(phrase.upper())

shout1 = Shouter("shout")
# prints "SHOUT"

shout2 = Shouter("shout")
# prints "SHOUT"

shout3 = Shouter("let it all out")
# prints "LET IT ALL OUT"

####################################################

can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for element in can_we_count_it:
  if hasattr(element, "count"):
    print(str(type(element)) + " has the count attribute!")
  else:
    print(str(type(element)) + " does not have the count attribute :(")
    

####################################################

class SearchEngineEntry:
  secure_prefix = "https://"
  def __init__(self, url):
    self.url = url

  def secure(self):
    return "{prefix}{site}".format(prefix=self.secure_prefix, site=self.url)

codecademy = SearchEngineEntry("www.codecademy.com")
wikipedia = SearchEngineEntry("www.wikipedia.org")

print(codecademy.secure())
# prints "https://www.codecademy.com"

print(wikipedia.secure())
# prints "https://www.wikipedia.org"

#########################################################

class Student:
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []
  
  def add_grade(self, grade):
    self.grade = grade

    if type(grade) is Grade:
      self.grades.append(grade)


roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

class Grade:
  minimum_passing = 65
  def __init__(self, score):
    self.score = score
  
  def is_passing(self, score):
    if self.score > minimum_passing:
      return "You Passed!"

pieter.add_grade(Grade(100))

'''
Great job! You’ve created two classes and defined their interactions. This is object-oriented programming! From here you could:

-Write a Grade method .is_passing() that returns whether a Grade has a passing .score.

-Write a Student method .get_average() that returns the student’s average score.

-Add an instance variable to Student that is a dictionary called .attendance, with dates as keys and booleans as values that indicate whether the student attended school that day.

-Write your own classes to do whatever logic you want!
'''
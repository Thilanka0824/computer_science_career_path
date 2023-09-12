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
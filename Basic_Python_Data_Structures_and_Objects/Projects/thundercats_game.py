class Thundercat:
  def __init__(self, name, super_power, health=100, strike=40):
    self.name = name
    self.health = health
    self.strike = strike
    self.super_power = strike * 1.5
    self.is_knocked_out = False

  def __repr__(self):
    return "{name} has {health} health hit points remaining. They have a {strike} strike force and a {super_power} super power strike!".format(name=self.name, health=self.health, strike=self.strike, super_power=self.super_power)
   

  def knocked_out(self):
    self.is_knocked_out = True

    if self.health != 0:
      self.health = 0
    print("{name} was knocked out!".format(name=self.name))


  def lose_health(self, amount):
    self.health -= amount

    if self.health <= 0:
      self.health = 0
      self.knocked_out()
    else:
      print("{name} now has {health} health.".format(name=self.name, health=self.health))


  def attack(self, opponent):

    if self.is_knocked_out:
      print("{name} can't attack because they're knocked out!".format(name=self.name))
      return

    if self.health > 0 and opponent.health > 0:
      print("{my_name} attacked {opp_name} for {damage} damage.".format(my_name=self.name, opp_name=opponent.name, damage=self.strike))
      opponent.lose_health(self.strike)


lion_o = Thundercat("Lion-O", "Sword", strike=50)
tygra = Thundercat("Tygra", "Invisibility")
cheetara = Thundercat("Cheetara", "Super Speed")
panthro = Thundercat("Panthro", "Super Strength")

print(lion_o)
print(tygra)
print(cheetara)
print(panthro)



class Mumraa:
  def __init__(self, name, type_of, strike, health=100):
    self.name = name
    self.type_of = type_of
    self.health = health
    self.strike = strike
    self.is_knocked_out = False

  def __repr__(self):
    return "{name} is a {type_of} with a max health of {health} and a strike force of {strike}.".format(name=self.name, type_of=self.type_of, health=self.health, strike=self.strike)


  def knocked_out(self):
    self.is_knocked_out = True

    if self.health != 0:
      self.health = 0
    print("{name} was knocked out!".format(name=self.name))


  def lose_health(self, amount):
    self.health -= amount

    if self.health <= 0:
      self.health = 0
      self.knocked_out()
    else:
      print("{name} now has {health} health.".format(name=self.name, health=self.health))


  def attack(self, opponent):

    if self.is_knocked_out:
      print("{name} can't attack because they're knocked out!".format(name=self.name))
      return

    if self.health > 0 and opponent.health > 0:
      print("{my_name} attacked {opp_name} for {damage} damage.".format(my_name=self.name, opp_name=opponent.name, damage=self.strike))
      opponent.lose_health(self.strike)


mummy_drone = Mumraa("Mummy", "drone", strike=15, health=30)
mummy_lieutenant = Mumraa("Big Mummy", "lieutenant", strike=25, health=50)
boss = Mumraa("Mumraa", "boss", strike=60, health=200)

print(mummy_drone)
print(mummy_lieutenant)
print(boss)

print(tygra.attack(mummy_drone))    

game_started = False

thundercats = [lion_o, tygra, cheetara, panthro]
mummies = [mummy_drone, mummy_lieutenant, boss]

thundercat_choice = input("Please choose a Thundercat to start the game.\n\nPress:\n1 for Lion-O\n2 for Tygra\n3 for Cheetara\n4 for Panthro\n\nPress Enter once you've chosen your Thundercat: ")

while thundercat_choice is 1:
  print("You chose Lion_O and the Sword of Omens!")
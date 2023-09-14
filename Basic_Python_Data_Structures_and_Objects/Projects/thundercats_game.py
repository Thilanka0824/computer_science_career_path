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




class Mumraa:
  def __init__(self, name, strike, health=100):
    self.name = name
    self.health = health
    self.strike = strike
    self.is_knocked_out = False
    


one = Thundercat("Lion-O", "Sword", strike=50)
two = Thundercat("Tygra", "Invisibility")
three = Thundercat("Cheetara", "Super Speed")
four = Thundercat("Panthro", "Super Strength")
print(one)
print(two)
print(three)
print(four)
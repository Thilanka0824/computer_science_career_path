#Writing a CSV File

access_log = [{'time': '08:39:37', 'limit': 844404, 'address': '1.227.124.181'}, {'time': '13:13:35', 'limit': 543871, 'address': '198.51.139.193'}, {'time': '19:40:45', 'limit': 3021, 'address': '172.1.254.208'}, {'time': '18:57:16', 'limit': 67031769, 'address': '172.58.247.219'}, {'time': '21:17:13', 'limit': 9083, 'address': '124.144.20.113'}, {'time': '23:34:17', 'limit': 65913, 'address': '203.236.149.220'}, {'time': '13:58:05', 'limit': 1541474, 'address': '192.52.206.76'}, {'time': '10:52:00', 'limit': 11465607, 'address': '104.47.149.93'}, {'time': '14:56:12', 'limit': 109, 'address': '192.31.185.7'}, {'time': '18:56:35', 'limit': 6207, 'address': '2.228.164.197'}]
fields = ['time', 'address', 'limit']


import csv

with open('logger.csv', 'w') as logger_csv:
  # fields = ['time', 'limit', 'address']
  log_writer = csv.DictWriter(logger_csv, fieldnames=fields)

  log_writer.writeheader()
  for item in access_log:
     log_writer.writerow(item)

  sentence = "I love programming!"

  print(sentence[7:])

fridge_contents = {"egg":12, "milk": 2, "apple": 6, "celery": 5}

for variable1, variable2 in fridge_contents.items():
    if variable1 in fridge_contents:
        print(fridge_contents[variable1])
    if variable2 in fridge_contents:
        print(fridge_contents[variable2])

with open('programming_languages.txt', 'w') as programming_languages_doc:

    programming_languages_doc.write('Python')

# All of our store items
all_items = [["Taffy", 1], ["Chocolate", 2], ["Cup", 5], ["Plate", 10], ["Bowl", 11], ["Silverware", 22]]

# Empty discounted_items list
discounted_items = []

# Your code here
for item in all_items:
  # print(item[1])
  if not item[1] % 2 == 0:
    discounted_items.append(item)
  # print(discounted_items)

# For testing purposes: print discounted list
print(discounted_items)

starting_money = 100
starting_num_items = 10
item_price = 4

starting_money = 100
starting_num_items = 10
item_price = 4


# Your code here
def buy_items(money_on_hand, treats_available, price_of_treat):
  num_bought = 0
  while num_bought < treats_available and money_on_hand >= price_of_treat:
    
      num_bought += 1
      money_on_hand -= price_of_treat
      
  return num_bought

total = buy_items(starting_money, starting_num_items, item_price)
print("You were able to buy " + str(total) + " items.")
  
# For testing purposes
total_1 = buy_items(100, 10, 4)
print("Test 1: " + str(total_1))
total_2 = buy_items(10, 10, 4)
print("Test 2: " + str(total_2))

class HashtagsCreator:
  
  def __init__(self,list_of_terms):
    self.hashtags = []
    
    for term in list_of_terms:
      # Fix this section of code
      if term[0] == "@" or term[0] == "#":
        self.hashtags.append("#" + term[1:])
      else:
        self.hashtags.append("#" + term)
      
  def list_hashtags(self):
    for hashtag in self.hashtags:
      print(hashtag)

# Do not edit testing code
test_hashtags = HashtagsCreator(["@codecademy", "#python", "programming", "#strings"])
test_hashtags.list_hashtags()

##############################

# Import random class
import random

class Number_Guesser:
  
  def __init__(self, player_names):
    self.player_guesses = {}

    # Adds names and -1 to player_guesses
    for name in player_names:
      self.player_guesses[name] = -1
      
    # Update to choose a random number
    self.secret_number = random.randint(1, 10)

  def add_player_guess(self, name, guess):
    # Fill in this method
    if name in self.player_guesses:
      self.player_guesses[name] = guess
    
  def print_answer(self):
    print(str(self.secret_number), "is the secret number!")
    
  def print_guesses(self):
    for player in self.player_guesses.items():
      if player[1] != -1:
        print(player[0], "guessed", str(player[1]))
      else:
        print(player[0], "needs to guess!") 

game1 = Number_Guesser(["Thuy", "Joe", "Diya"])
game1.add_player_guess("Roger", 10)
game1.add_player_guess("Diya", 8)
game1.add_player_guess("Thuy", 1)
game1.add_player_guess("Joe", 5)
game1.print_guesses()
game1.print_answer()

#You’ve received a CSV of names, email addresses, and phone numbers, and you need to change it to a more person-readable format. The file is named employees.csv.

#The file looks like:

#Name,Email,Phone Number
#Roger Smith,wigginsryan@yahoo.com,(555) 123-4567
#Dan Meki,dmeki@hotmail.com,(555) 234-5678
...

#Your task is to only take the Name and Phone Number fields and print out each line as:

#Roger Smith: (555) 123-4567

#You must:

#Use the correct syntax for processing a CSV file.
#Use a DictReader in your solution.
#Print a line for every entry in the file!

import csv

with open('employees.csv') as employees_csv:
  reader = csv.DictReader(employees_csv)
  for row in reader:
    print(row['Name'] + ": " + row['Phone Number'])
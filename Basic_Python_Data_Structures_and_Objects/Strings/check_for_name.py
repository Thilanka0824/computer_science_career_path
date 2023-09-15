#Write a function called check_for_name that takes two strings as parameters named sentence and name. The function should return True if name appears in sentence in all lowercase letters, all uppercase letters, or with any mix of uppercase and lowercase letters. The function should return False otherwise.

#For example, the following three calls should all return True:

# Write your check_for_name function here:

def check_for_name(sentence, name):
  split_sentence = sentence.lower().split(" ")
  for word in split_sentence:
    if word == name.lower():
      return True
  return False
  
# Uncomment these function calls to test your  function:
print(check_for_name("My name is Jamie", "Jamie"))
# should print True
print(check_for_name("My name is jamie", "Jamie"))
# should print True
print(check_for_name("My name is Samantha", "Jamie"))
# should print False

'''
#Alternate solution

def check_for_name(sentence, name):
    return name.lower() in sentence.lower()
'''
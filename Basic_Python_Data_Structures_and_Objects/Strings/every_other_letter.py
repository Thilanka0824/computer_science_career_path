#Create a function named every_other_letter that takes a string named word as a parameter. The function should return a string containing every other letter in word.

# Write your every_other_letter function here:
def every_other_letter(word):
  final_string = ""
  for index, letter in enumerate(word):
    if index % 2 == 0:
       final_string += letter
      #  print(final_string)
  return final_string

# Uncomment these function calls to test your function:
print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print 

'''
#Alternate solution

def every_other_letter(word):
  every_other = ""
    for i in range(0, len(word), 2)
      every_other += word[i]
  return every_other
'''
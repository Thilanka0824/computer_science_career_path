#Write a function named reverse_string that has a string named word as a parameter. The function should return word in reverse.

# Write your reverse_string function here:
def reverse_string(word):
  reversed_str = ""
  
  for i in range(len(word)-1, -1, -1):
    reversed_str += word[i]
  return reversed_str


# Uncomment these function calls to test your  function:
print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print
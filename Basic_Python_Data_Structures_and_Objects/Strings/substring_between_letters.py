#Write a function named substring_between_letters that takes a string named word, a single character named start, and another character named end. This function should return the substring between the first occurrence of start and end in word. If start or end are not in word, the function should return word.

#For example, substring_between_letters("apple", "p", "e") should return "pl".

 # Write your substring_between_letters function here:
def substring_between_letters(word, start, end):
    start_index = word.find(start)
    end_index = word.find(end)
    
    if start_index == -1 or end_index == -1:
      return word
    
    if word.find(start) and word.find(end):
      return word[start_index + 1:end_index]

# Uncomment these function calls to test your function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"

'''
#alternate solution

def substring_between_letters(word, start, end):
  start_ind = word.find(start)
  end_ind = word.find(end)
  if start_ind > -1 and end_ind > -1:
    return(word[start_ind+1:end_ind])
  return word
'''
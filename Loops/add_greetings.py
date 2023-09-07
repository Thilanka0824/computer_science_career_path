#Create a function named add_greetings() which takes a list of strings named names as a parameter.
#In the function, create an empty list that will contain each greeting. Add the string 'Hello, ' in front of each name in names and append the greeting to the list.
#Return the new list containing the greetings.

#Write your function here
def add_greetings(names):
    name_list = []
    for name in names:
        name_list.append("Hello, " + name)
    return name_list


#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))
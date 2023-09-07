#Write a function called delete_starting_evens() that has a parameter named my_list.
#The function should remove elements from the front of my_list until the front of the list is not even. The function should then return my_list.
#For example if my_list started as [4, 8, 10, 11, 12, 15], then delete_starting_evens(my_list) should return [11, 12, 15].
#Make sure your function works even if every element in the list is even!

#Write your function here
def delete_starting_evens(my_list):
    if (len(my_list) > 0):
        for num in my_list:
            if (num % 2 == 0):
                my_list = my_list[1:]
            else:
                return my_list
        return my_list
    else:
        return "Empty list, Bozo"
#Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))
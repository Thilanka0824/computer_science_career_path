#Create a function called middle_element that has one parameter named my_list.
#If there are an odd number of elements in my_list, the function should return the middle element. If there are an even number of elements, the function should return the average of the middle two elements.

#Write your function here
def middle_element(my_list):
    if (len(my_list) % 2 == 0):
        sum = my_list[int(len(my_list) / 2)] + my_list[int(len(my_list) / 2) - 1]
        return sum / 2
    else:
        return my_list[int(len(my_list) / 2)]


#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))

"""
We used modulus to determine if the list had an even or odd number of elements. After determining this, for an odd number of elements, we calculate the middle index and return the middle element from the list. For an even number of elements, we calculate the index of the element close to the middle and the other element close to the middle (by subtracting 1 from the middle calculation). We get the values at those indices and calculate the average.

Note that the math to find the middle index is a bit tricky. In some cases, when we divide by 2, we would get a double. For example, if our list had 3 items in it, then 3/2 would give us 1.5. The middle index should be 1, so in order to go from 1.5 to 1, we cast 1.5 as an int. In total, this is int(len(my_list)/2).
"""
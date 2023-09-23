from LinkedList import LinkedList

# Complete this function:
def nth_last_node(linked_list, n): # returns the nth to last node of a linked list
  current = None # the nth to last node
  tail_seeker = linked_list.head_node # the node that is n nodes ahead of the current node
  count = 1 # the number of nodes between the current node and the tail seeker

  while tail_seeker: 
    tail_seeker = tail_seeker.get_next_node() # set the tail seeker to the next node
    count += 1 
    if count >= n + 1: 
      if current is None: 
        current = linked_list.head_node # set the current node to the head node
      else: 
        current = current.get_next_node() # set the current node to the next node
  return current # return the current node

#The way this function works is by having two pointers, current and tail_seeker. The tail_seeker pointer is n nodes ahead of the current pointer. When the tail_seeker pointer reaches the end of the linked list, the current pointer will be n nodes from the end of the linked list. 

# This is because the tail_seeker pointer is n nodes ahead of the current pointer. So, when the tail_seeker pointer reaches the end of the linked list, the current pointer will be n nodes from the end of the linked list.

def generate_test_linked_list():
  linked_list = LinkedList()
  for i in range(50, 0, -1):
    linked_list.insert_beginning(i)
  return linked_list

# Use this to test your code:
test_list = generate_test_linked_list()
print(test_list.stringify_list())
nth_last = nth_last_node(test_list, 45)
print(nth_last.value)

#The exact variable names aren’t important, and the internal implementation could be written in a number of ways, but the important part is that we are able to complete this problem efficiently, in O(n) time (we must iterate through the entire list once), and O(1) space complexity (we always use only three variables no matter what size the linked list is: two pointers and a counter).
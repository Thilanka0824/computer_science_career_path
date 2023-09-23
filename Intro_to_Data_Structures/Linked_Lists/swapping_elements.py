# Define your Node class below:
class Node:
  def __init__(self, value, next_node=None):
    self.value = value # the value at the current node
    self.next_node = next_node # the next node in the linked list

  def get_value(self): # returns the value stored at the current node
    return self.value 

  def get_next_node(self): # returns the next node in the linked list
    return self.next_node

  def set_next_node(self, next_node): # sets the next node in the linked list
    self.next_node = next_node 

my_node = Node(44) 
print(my_node.get_value()) 

# Create your LinkedList class below:
class LinkedList: 
  def __init__(self, value=None): 
    self.head_node = Node(value) # the head node of the linked list

  def get_head_node(self): # returns the head node of the linked list
    return self.head_node
  
  # Add your insert_beginning and stringify_list methods below:
  def insert_beginning(self, new_value): # inserts a new node at the beginning of the linked list 
    new_node = Node(new_value) # create a new node with the new value
    new_node.set_next_node(self.head_node) # set the new node's next node to the current head node
    self.head_node = new_node # set the head node to the new node

  def stringify_list(self): # returns a string representation of the linked list
    string_list = "" 
    current_node = self.get_head_node() # start at the head node
    while current_node: 
      if current_node.get_value() != None: # if the current node's value is not None
        string_list += str(current_node.get_value()) + "\n" # add the current node's value to the string list
        current_node = current_node.get_next_node() # set the current node to the next node
    return string_list 


  # Define your remove_node method below:
  def remove_node(self, value_to_remove): # removes the node with the value to remove from the linked list
    current_node = self.get_head_node() # start at the head node
    if current_node.get_value() == value_to_remove: # if the head node is the value to remove
      self.head_node = current_node.get_next_node() #
    else:
      while current_node: # while there is a current node
        next_node = current_node.get_next_node() # set the next node to the current node's next node
        if next_node.get_value() == value_to_remove: # if the next node's value is the value to remove
          current_node.set_next_node(next_node.get_next_node()) # set the current node's next node to the next node's next node
          current_node = None # set the current node to None
        else:
          current_node = next_node # set the current node to the next node
    
def remove_multiple_nodes(self, values_to_remove):
  current_node = self.get_head_node()


'''
Swapping Elements in a Linked List
Learn how to swap two nodes in a singly linked list in Python.

Since singly linked lists only have pointers from each node to its next node, swapping two nodes in the list isn’t as easy as doing so in an array (where you have access to the indices). You not only have to find the elements, but also reset their surrounding pointers to maintain the integrity of the list. This means keeping track of the two nodes to be swapped as well as the nodes preceding them.

Given a linked list and the elements to be swapped (val1 and val2), we need to keep track of four values:

node1: the node that matches val1
node1_prev: node1‘s previous node
node2: the node that matches val2
node2_prev: node2‘s previous node
Given an input of a linked list, val1, and val2, the general steps for doing so is as follows:

Iterate through the list looking for the node that matches val1 to be swapped (node1), keeping track of the node’s previous node as you iterate (node1_prev)
Repeat step 1 looking for the node that matches val2 (giving you node2 and node2_prev)
If node1_prev is None, node1 was the head of the list, so set the list’s head to node2
Otherwise, set node1_prev‘s next node to node2
If node2_prev is None, set the list’s head to node1
Otherwise, set node2_prev‘s next node to node1
Set node1‘s next node to node2‘s next node
Set node2‘s next node to node1‘s next node
Finding the Matching and Preceding Nodes
Let’s look at what implementing steps 1 and 2 looks like. In order to swap the two nodes, we must first find them. We also need to keep track of the nodes that precede them so that we can properly reset their pointers. (We will use the Node class’s .get_next_node() method in order to access the next node.)

We will start by setting node1 equal to the head of the list, and then creating a while loop that runs while node1 isn’t None. Inside the loop, we will check if node1‘s value matches val1. If so, we break out of the loop as we have found the correct node. If there is no match, we update node1_prev to be node1 and move node1 to its next node:

def swap_nodes(input_list, val1, val2):
  node1 = input_list.head_node
  node2 = input_list.head_node
  node1_prev = None
  node2_prev = None

  while node1 is not None:
    if node1.get_value() == val1:
      break
    node1_prev = node1
    node1 = node1.get_next_node()
'''


'''
Updating the Preceding Nodes’ Pointers
Our next step is to set node1_prev and node2_prev‘s next nodes, starting with node1_prev. We’ll begin by checking if node1_prev is None. If it is, then the node1 is the head of the list, and so we will update the head to be node2. If node1_prev isn’t None, then we set its next node to node2:

if node1_prev is None:
  input_list.head_node = node2
else:
  node1_prev.set_next_node(node2);
'''

'''
After this step, we have finished updating the pointers that point to our swapped nodes. The next step will be to update the pointers from them.
'''

'''
Updating the Nodes’ Next Pointers
The last step is to update the pointers from node1 and node2. This is relatively simple, and mirrors a swapping function for an array in that we will use a temporary variable.
'''

'''
Edge Cases
We have completed the basic swap algorithm in Python! However, we haven’t accounted for some edge cases. What if there is no matching node for one of the inputs? The current swap_nodes() function will not run because we will try to access the next node of a node that is None. (Remember that our initial while loop only breaks if the matching node is found. Otherwise, it runs until the node is None.)

Thankfully this has a quick fix. We can put in an if that checks if either node1 or node2 is None. If they are, we can print a statement that explains a match was not found, and return to end the method. We can put this right after the while loops that iterate through the list to find the matching nodes:

if (node1 is None or node2 is None):
  print("Swap not possible - one or more element is not in the list")
  return

The last edge case is if the two nodes to be swapped are the same. While our current implementation will run without error, there’s no point in executing the whole function if it isn’t necessary. We can add a brief check at the beginning of the function that checks if the val1 is the same as val2, and then return to end the function:

if val1 == val2:
  print("Elements are the same - no swap needed")
  return

'''



def swap_nodes(input_list, val1, val2):
  print(f'Swapping {val1} with {val2}')

  node1_prev = None
  node2_prev = None
  node1 = input_list.head_node
  node2 = input_list.head_node

  if val1 == val2:
    print("Elements are the same - no swap needed")
    return

  while node1 is not None:
    if node1.get_value() == val1:
      break
    node1_prev = node1
    node1 = node1.get_next_node()

  while node2 is not None:
    if node2.get_value() == val2:
      break
    node2_prev = node2
    node2 = node2.get_next_node()

  if (node1 is None or node2 is None):
    print("Swap not possible - one or more element is not in the list")
    return

  if node1_prev is None:
    input_list.head_node = node2
  else:
    node1_prev.set_next_node(node2)

  if node2_prev is None:
    input_list.head_node = node1
  else:
    node2_prev.set_next_node(node1)

  temp = node1.get_next_node()
  node1.set_next_node(node2.get_next_node())
  node2.set_next_node(temp)


ll = LinkedList()
for i in range(10):
  ll.insert_beginning(i)

print(ll.stringify_list())
swap_nodes(ll, 9, 5)
print(ll.stringify_list())
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



# 
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




# Test your code by uncommenting the statements below - did your list print to the terminal?
# ll = LinkedList(5)
# ll.insert_beginning(70)
# ll.insert_beginning(5675)
# ll.insert_beginning(90)
# print(ll.stringify_list())

# my_node.set_next_node(99)
# print(my_node.get_next_node())



trod_node = Node("Trod")
lerman_node = Node("Katlin")
bailey_node = Node("Bae")
print(trod_node.get_value())
print(lerman_node.get_value())
print(bailey_node.get_value())

fam_ll = LinkedList(1)
fam_ll.insert_beginning(trod_node.get_value())
fam_ll.insert_beginning(lerman_node.get_value())
fam_ll.insert_beginning(bailey_node.get_value())
print(fam_ll.stringify_list())

fam_ll.remove_node(1)
print(fam_ll.stringify_list())

yacko = Node("likes to yak")
wacko = Node("has a penchant for hoarding snacks")
dot = Node("enjoys spending time in movie lots")

yacko.set_next_node(dot)
dot.set_next_node(wacko)

dots_data = yacko.get_next_node().get_value()
wackos_data = dot.get_next_node().get_value()
print(dots_data)
print(wackos_data)

yak_to_wak = yacko.get_next_node().get_next_node().get_value() # here we are accessing the value of the node that is two nodes away from yacko (wacko)

print(yak_to_wak)

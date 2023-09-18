# Define your Node class below:
class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next_node(self):
    return self.next_node

  def set_next_node(self, next_node):
    self.next_node = next_node

my_node = Node(44)
print(my_node.get_value())

# Create your LinkedList class below:
class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)

  def get_head_node(self):
    return self.head_node
  
  # Add your insert_beginning and stringify_list methods below:
  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node

  def stringify_list(self):
    string_list = ""
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"
        current_node = current_node.get_next_node()
    return string_list


# Test your code by uncommenting the statements below - did your list print to the terminal?
ll = LinkedList(5)
ll.insert_beginning(70)
ll.insert_beginning(5675)
ll.insert_beginning(90)
print(ll.stringify_list())

my_node.set_next_node(99)
print(my_node.get_next_node())

  # Define your remove_node method below:
def remove_node(self, value_to_remove):
    current_node = self.get_head_node()
    if current_node.get_value() == value_to_remove:
      self.head_node = current_node.get_next_node()
    else:
      while current_node:
        next_node = current_node.get_next_node()
        if next_node.get_value() == value_to_remove:
          current_node.set_next_node(next_node.get_next_node())
          current_node = None
        else:
          current_node = next_node
    
def remove_multiple_nodes(self, value_to_remove):
  current_node = self.get_head_node()



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

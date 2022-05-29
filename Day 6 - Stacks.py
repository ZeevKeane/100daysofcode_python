from node import Node

#  the coding day started with Mathematical fundamentals of Data Science - intro to probability, i learned of the difference between union, intersection, and complement. As well as, mutually exclusive events and the difeference between dependence and independence. This was then concluded with leanring of the addition rule. 
# P(a or b) = P(a) + P(b) - P(a and b) //// if not mutualy exclusive 
# P(a or b) = P(a) + P(b) //// for mutually exclusive. 



# CS102 - Stacks

#1
# Add your Stack class below:
class Stack(Node):
  def __init__(self, top_item=None):
    self.top_item = top_item

  def peek(self):
    return self.top_item.get_value()
  
  
#2

class Stack:
  def __init__(self):
    self.top_item = None
  
  # Define your push() and pop() methods below:
  def push(self, value):
    item = Node(value)
    item.set_next_node(self.top_item)
    self.top_item = item

  def pop(self):
    item_to_remove = self.top_item
    self.top_item = item_to_remove.get_next_node()
    return item_to_remove.value
  
  
  def peek(self):
    return self.top_item.get_value()
  
  
  
  
  
  

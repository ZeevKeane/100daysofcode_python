from linked_list import Node, LinkedList
from blossom_lib import flower_definitions 

class HashMaps:
  def __init__(self, size):
    self.array_size = size
    self.array = [LinkedList() for item in range(self.array_size)]

  # get to hash
  def hash(self, key):
    encoded = key.encode()
    hashed = sum(encoded)
    return hashed

  def compress(self, hash_value):
    return hash_value % self.array_size

  # get to interact with the hash
  def assign(self, key, value):
    array_index = self.compress(self.hash(key))
    payload = Node([key, value])
    list_at_array = self.array[array_index]
    for l in list_at_array:
      if l[0] == key:
        l[1] = value
        return
    list_at_array.insert(payload)



  def retrieve(self, key):
    array_index = self.compress(self.hash(key))
    list_at_index = self.array[array_index]
    for l in list_at_index:
      if l[0] == key:
        return l[1]
      else:
        return None


blossom = HashMaps(len(flower_definitions))

for flower in flower_definitions:
  blossom.assign(flower[0], flower[1])


print(blossom.retrieve('daisy'))



from contextlib import contextmanager 
  
# class-based context manager with error handling (*exc -exceptions) 

class PoemFiles:

  def __init__(self, poem_file, mode):
    print(' \n -- Starting up a poem context manager -- \n')
    self.file = poem_file
    self.mode = mode

  def __enter__(self):
    print(' \n --  Opening poem file -- \n')
    self.opened_poem_file = open(self.file, self.mode)
    return self.opened_poem_file

  def __exit__(self, exc_type, exc_value, traceback):
    print(exc_type, exc_value, traceback, '\n')
    # Write your code below: 
    if isinstance(exc_value, AttributeError):
      self.opened_poem_file.close()
      return True

# with PoemFiles('poem.txt', 'r') as file:
#   print("---- Exception data below ---- \n ")
#   print(file.uppercasewords())

# with PoemFiles('poem.txt', 'r') as file2:
#   print(file2.read())
#   print(" \n ---- Exception data below ---- \n ")


#contextlib


@contextmanager
def poem_files(file, mode):
  print('Opening File')
  open_poem_file = open(file, mode)
  try:
    yield open_poem_file
  finally:
    print('Closing File')
    open_poem_file.close()




# with poem_files('poem.txt', 'a') as opened_file:
#  print('Inside yield')
#  opened_file.write('Rose is beautiful, Just like you.')


from stack import Stack

print("\nLet's play Towers of Hanoi!!")

#Create the Stacks
stacks = []

left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")

stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

#Set up the Game
num_disks = int(input("\nHow many disks do you want to play with?\n"))

while num_disks < 3:
  num_disks = int(input("Enter a number greater than or equal to 3\n"))


for i in range(num_disks, 0, -1):
  disk = f"Disk {i}"
  left_stack.push(disk)

# print(left_stack.peek())

num_optimal_moves = 2**num_disks - 1

print(f"\nThe fastest you can solve this game is in {num_optimal_moves} moves")

#Get User Input
        
def get_input():
  choices = [stack.get_name()[0] for stack in stacks]

  while True:

    for s in range(len(stacks)):
      row_name = stacks[s].get_name()
      row_letter = row_name[0]
      print(f"Enter {row_letter} for {row_name}")

    user_input = input("")

    if user_input in choices:
      for i in range(len(stacks)):
        if user_input == choices[i]:
          return stacks[i]
        
    

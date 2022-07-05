# fibonacci:
# define the fibonacci() function below...

def fibonacci(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fibonacci(n-2) + fibonacci(n-1)



fibonacci(5)
# set the appropriate runtime:
# 1, logN, N, N^2, 2^N, N!
fibonacci_runtime = "2^N"

# binary search trees:
# Define build_bst() below...
def build_bst(my_list):
  if not my_list:
      return "No Child"
  middle_idx = int(len(my_list)/2)
  middle_value = my_list[middle_idx]
    
  print("Middle index: {0}".format(middle_idx))
  print("Middle value: {0}".format(middle_value))
  left_half_of_list = my_list[:middle_idx]
  right_half_of_list = my_list[middle_idx + 1:]
  
  tree_node = {"data": middle_value}
  tree_node["left_child"] = build_bst(left_half_of_list)
  tree_node["right_child"] = build_bst(right_half_of_list)

  return tree_node

# For testing
sorted_list = [12, 13, 14, 15, 16]
binary_search_tree = build_bst(sorted_list)
print(binary_search_tree)

# fill in the runtime as a string
# 1, logN, N, N*logN, N^2, 2^N, N!
runtime = "N*logN"

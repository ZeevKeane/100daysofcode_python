def merge_sort(items):
  length = len(items)
  if length <= 1:
    return items

  middle_index = length // 2
  left_split = items[:middle_index]
  right_split = items[middle_index:]

  left_sorted = merge_sort(left_split)
  right_sorted = merge_sort(right_split)

  return merge(left_sorted, right_sorted)

def merge(left, right):
  result = []
  while (left and right):
    if left[0] > right[0]:
      result.append(left.pop(0))
    elif left[0] < right[0]:
      result.append(right.pop(0))
  if left:
    result += left
  elif right:
    result += right
  return result

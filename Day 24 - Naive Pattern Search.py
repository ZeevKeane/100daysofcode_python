def pattern_search(text, pattern):
  print("Input Text:", text, "Input Pattern:", pattern)
  for index in range(len(text)):
    print("Text Index:", index)
    match_count = 0
    for char in range(len(pattern)):
      print("Pattern Index:", char)
      if pattern[char] == text[index + char]:
        print("Matching index found")
        print("Match Count:", match_count)
        match_count += 1
      else:
        break
    if match_count == len(pattern):
      print(pattern, "found at index", index)

      
def pattern_search_case(text, pattern,case_senesitive=True):
  for index in range(len(text)):
    match_count = 0
    if case_senesitive:
      PATTERN = pattern.upper()
      lower_pattern = pattern.lower()
      for char in range(len(pattern)):
        if lower_pattern[char] == text[index + char] or PATTERN[char] == [index + char]:
            match_count += 1
        else:
            break

    for char in range(len(pattern)):
      if pattern[char] == text[char + index]:
        match_count += 1
      else:
        break
    if match_count == len(pattern):
      print(pattern, "found at index", index)

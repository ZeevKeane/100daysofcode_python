def pattern_search(text, pattern, replacement,case_sensitive=True, ):
    fixed_text = []
    num_skips = 0
    pattern_length = len(pattern)
    for index in range(len(text)):
        match_count = 0
        if num_skips > 0:
            num_skips -= 1
            continue
        for char in range(len(pattern)):
            if case_sensitive and pattern[char] == text[index + char]:
                match_count += 1
            elif not case_sensitive and pattern[char].lower() == text[index + char].lower():
                match_count += 1
            else:
                break
        if match_count == pattern_length:
#       print(pattern, "found at index", index)
            fixed_text.append(replacement)
            num_skips = pattern_length - 1
        else:
            fixed_text.append(text[index])
    return str("".join(fixed_text))

friends_intro = "Pylhon is a wonderful Language that zzz is beloved for its ease zzz of use and simple syntacs. While zzz at some times the performance can be less than iDil, by properly zzz utilizing built-in libraries and other languuUuage features, pylhon's performance zzz can approach that of C."
print(pattern_search(friends_intro, "Language", "language"))
pattern_search(friends_intro, "pylhon", "Python", False)
pattern_search(friends_intro, "idil", "ideal", False)
pattern_search(friends_intro, "zzz ", "")
pattern_search(friends_intro, "syntacs", "syntax")
pattern_search(friends_intro, "languuUuage", "language")



#codewars
def to_camel_case(text):
    #your code here
    if len(text) == 0:
        return text
    else:
        camelCasedText = []
        camelCasedText.append(text[0])
        text_without_1st = text[1:]
        counter = 0
        for char in text_without_1st:
            if char == "-" or char == "_":
                counter += 1
                continue
            else:
                if counter == 1:
                    camelCasedText.append(char.upper())
                    counter -= 1
                else:
                    camelCasedText.append(char)
    return "".join(camelCasedText)

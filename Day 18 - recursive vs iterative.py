
# implementing an iterative version of factorial()
def factorial(n):
    result = 1
    if n < 0:
        ValueError("Inputs 0 or greater only")
    for n in range(2,n+1):
        result *= n
    return result

# implementing an iterative version of fibonacci()
def fibonacci(f):
    sequence = [0,1]
    if f < 0:
        ValueError("Input 0 or greater only!")
    if f == 1 or f == 2:
        return sequence[f-1]
    else:
        for n in range(3,f+2):
            sequence.append(sequence[-1] + sequence[-2])
    return sequence[f]

# implementing a recursive version of sum_digits()
def sum_digits(n):
    if n < 0:
        ValueError("Inputs 0 or greater only!")
    if n < 10:
        return n
    else:
        last_digit = n % 10
        return sum_digits(n // 10) + sum_digits(last_digit)

# implementing a recursive version of find_min()
def find_min(my_list, min=None):
    if not my_list:
        return min
    else:
        if not min or (my_list[0] < min):
            min = my_list[0]
        return find_min(my_list[1:], min)

# implementing a recursive version of is_palindrome()
def is_palindrome(my_string):
    if len(my_string) < 2:
        return True
    else:
        if my_string[0] != my_string[-1]:
            return False
        return is_palindrome(my_string[1:-1])

def create_phone_number(n):
    #your code here
    counter = 0
    length_of_input = len(n)
    start_of_cpn = ["("]
    middle_of_cpn = [")", " "]
    end_of_cpn = ["-"]
    while counter < length_of_input:
        if counter < 3:
            start_of_cpn.append(str(n[counter]))
            counter += 1
        elif counter >= 3 and counter < 6:
            middle_of_cpn.append(str(n[counter]))
            counter += 1
        else:
            end_of_cpn.append(str(n[counter]))
            counter += 1
    cpn = start_of_cpn + middle_of_cpn + end_of_cpn
    return "".join(cpn)

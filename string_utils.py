def split_before_each_uppercases(formula):
    split_formula = []
    if not formula:
        return split_formula

    start_index = 0
    for i in range(1, len(formula)):
        if formula[i].isupper():
            split_formula.append(formula[start_index:i])
            start_index = i

    split_formula.append(formula[start_index:])
    return split_formula

def split_at_first_digit(formula):
    digit_location = 1 

    
    for i in range(1, len(formula)):
        if formula[i].isdigit():
          
            digit_location = i
            break 
        else:
          
            digit_location += 1

  
    if digit_location == len(formula):
        return formula, 1
    else:
        prefix = formula[:digit_location]
        numeric_part = int(formula[digit_location:])
        return prefix, numeric_part

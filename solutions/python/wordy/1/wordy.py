import re
import operator

OPERATIONS = {
    "plus": operator.add, 
    "minus": operator.sub, 
    "divided": operator.floordiv,  
    "multiplied": operator.mul
    }

PREAMBLE = "What is "

def answer(question):
    cleaned_numbers, ops_order = check_question(question)
    result = cleaned_numbers[0]
    if ops_order:
        for ii, op in enumerate(ops_order):
            result = OPERATIONS[op](result, cleaned_numbers[ii+1])
    return result

def check_question(question):
    if PREAMBLE not in question:
        raise ValueError("syntax error")
    else:
        _, *rem = question.split(PREAMBLE)
    
    # raw number check
    raw_numbers = re.findall(r"-?\d(?:\s*\d)*", *rem)

    cleaned_numbers = []

    # try converting these raw numbers into integers and throw an error if there's a failure
    for num in raw_numbers:
        try:
            cleaned_numbers.append(int(num))
        except:
            raise ValueError("syntax error")
    
    rem_split = rem[0].split()

    # remove the term "by"
    rem_split = [ii for ii in rem_split if ii != "by"]
    
    # get all the operations
    ops_order = [ii.replace("?", "") for ii in rem_split if ii.replace("?", "") in OPERATIONS.keys()]            

    # error for when the operation is not recognized [raise error], or if there are no operations, but a single number is provided [return the number]
    if not ops_order:
        if len(rem_split) == 1 and "?" in rem_split[0]:
            return [int(rem_split[0].replace("?", ""))], ops_order
        else:
            raise ValueError("unknown operation")
    else:
        # check if an operation term is preceded or followed by a number
        for operation in ops_order:
            try:
                ind = rem_split.index(operation)
                # previous
                int(rem_split[ind - 1])
                # next
                int(rem_split[ind + 1]) if "?" not in rem_split[ind + 1] else int(rem_split[ind + 1].replace("?", ""))
            except:
                raise ValueError("syntax error")

    # return the cleaned numbers and the operations to be performed in order
    return cleaned_numbers, ops_order

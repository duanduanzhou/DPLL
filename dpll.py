"""
This file implements DPLL algorithm and solves the puzzle encoded in CNF. 
"""

from fileprocessor import process_dimacs

# Reference: https://stackoverflow.com/questions/12547160/how-does-the-dpll-algorithm-work
def add_encoding(encodings, elem):
    # add new encodings
    new_encodings = list()
    new_encoding = list()
    for encoding in encodings:
        if elem in encoding:
            continue
        # if already assigned, then remove negation
        new_encoding = list(x for x in encoding if x != -elem)
        if new_encoding is not None:
            new_encodings.append(new_encoding)
    return new_encodings

def dpll_algo(encodings, assign):
    # Explore the solutions recursively using DPLL
    if not encodings:  # SAT if all processed
        return assign
    
    # Check for unsatisfiable encoding
    unsat = False
    for encoding in encodings:
        if not encoding: # if encoding is empty
            unsat = True
            break 
    if unsat:
        return False

    # Unit-preference rule
    # check if there is a single element
    single_encoding = None
    for elem in encodings:
        if len(elem) == 1:  # if single, get the first elem
            single_encoding = encoding[0]
            break 

    # single encoding as the base case
    if single_encoding is not None:
        assign[single_encoding] = True
        new_encodings = add_encoding(encodings, single_encoding)
        result = dpll_algo(new_encodings, assign)
        return result 

    # if no single encoding, just select the first 
    selected = encodings[0][0]
    true_encodings = add_encoding(encodings, selected)
    assign[selected] = True
    solution = dpll_algo(true_encodings, assign)
    if solution: # SAT 
        return solution
    assign.remove(selected)  # unselect 
    false_encodings = add_encoding(encodings, -selected)
    assign[selected] = False
    solution = dpll_algo(false_encodings, assign)
    return solution

def apply_dpll(path):
    # Apply DPLL to the file 
    encodings = process_dimacs(path)
    assign = dict()
    solution = dpll_algo(encodings, assign)
    result = list()
    if solution != None:
        for encoding in solution:
            if solution[encoding] is not False:
                result.append(str(encoding))
        return "SAT\n" + " ".join(result)
    else:
        return "UNSAT"

def main():
    result = apply_dpll("cnf.txt")
    print(result)

if __name__ == "__main__":
    main()


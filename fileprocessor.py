"""
This file implements a DIMACS file processor. 
"""

def process_dimacs(path):
    # Reference: https://stackoverflow.com/questions/28890268/parse-dimacs-cnf-file-python
    with open(path, "r") as file:
        content = file.readlines()
    result = list()  # store parsed encodings
    encoding = list() # store encoding
    for line in content:
        stripped = line.strip()
        tokens = stripped.split()
        if stripped.startswith(("c", "p")):
            continue
         # remove the last zero
        encoding = list(int(elem) for elem in tokens if elem != "0") 
        result.append(encoding)
    return result

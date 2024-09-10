import helloworld
import csv

def main():
    for i in range(2, 42, 2):
        if i == 40:
            print(i)
        else:
            print(i, end=', ')

main()

# LISTS
# basically vectors or array-lists
# can grow/shrink in size --> dynamic!
# mixed types
# lists are objects, everything is an object!
fibs = [1, 1, 2, 3, 5, 8]

print(fibs, type(fibs))
print(fibs[0], fibs[-1])

for val in fibs:
    print(val, end=" ")
print()

for i in range(len(fibs)):
    print(i, ":", fibs[i], end=" | ")
print()

for i, val in enumerate(fibs): # tuple unpacking
    print(i, ":", val, end=" | ")
print()

# built-in funcs
# sum(), min(), max(), len(), sorted(), etc.
print(sorted(fibs, reverse=True)) # sorts a copy DOES NOT MODIFY THE LIST; MAKES A COPY!

# list methods
# method invocation syntax: <object>.<method>()

# fibs.sort(reverse=True) # sort fibs in place
# print(fibs)

# OOP on Tuesday

print(fibs.index(5))
fibs.pop(4) # pos based removal
print(fibs)
fibs.insert(4, 5)
print(fibs)
fibs.remove(8) # FIRST OCCURENCE ONLY
print(fibs)
fibs.append(8)
print(fibs)

# 2D LISTS (nested lists)
matrix = [[0, 1, 2], 
          [3, 4, 5]]
print(matrix[0], matrix[0][1])

# FILE IO
# often we want to open a file and read its contents into memory
# let's start with a CSV (comma separated value)

def load_table(filename):
    table = []
    # 1. open the file
    infile = open(filename, "r") # Read
    reader = csv.reader(infile)
    for row in reader:
        # TASK: use try/except block to convert strings to numeric type appropriately
        convert_to_numeric(row)
        print(row)
        table.append(row)
    # 2. process the file
    # let's use the csv module to read the file rows
    
    # 3. close the file
    infile.close()
    return table # ALL STRINGS!

def convert_to_numeric(values):
    for i in range(len(values)):
        try:
            numeric_val = float(values[i])
            values[i] = numeric_val
        except ValueError as e: # Failed to convert. 
            print(e)

def write_table(table, filename):
    outfile = open(filename, "w")
    writer = csv.writer(outfile)
    writer.writerows(table)
    outfile.close()

table = load_table("data.csv")
print(table)
write_table(table, "data_copy.csv") # same file but with floats
# def pretty_print(table):



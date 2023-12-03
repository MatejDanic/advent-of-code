
schematic = []

with open("input.txt", 'r') as file:
    for line in file:
        line = line.strip()
        schematic.append([char for char in line])

        
def is_symbol(char):
    return not char.isnumeric() and not char == '.'

def is_symbol_adjacent(row, first_column, last_column):
    for i in range (row-1, row+2):
        for j in range (first_column-1, last_column+2):
            if (i >= 0 and j >= 0 and i < len(schematic) and j < len(schematic[i])):
                #print("(" + str(i) + ", " + str(j) + ") = " + str(schematic[i][j]) + " is symbol? " + str(is_symbol(schematic[i][j])))
                if is_symbol(schematic[i][j]):
                    return True
    return False

sum = 0

for i in range(len(schematic)):
    print(schematic[i])
    number = ""
    first_column = None
    for j in range(len(schematic[i])):
        if schematic[i][j].isnumeric():
            if first_column is None:
                first_column = j
            last_column = j
            number += schematic[i][j]
            # end of row
            if j == len(schematic[i])-1:
                if is_symbol_adjacent(i, first_column, last_column):
                    sum += int(number)
                    print(sum)
        # end of number
        else: 
            if number.isnumeric():
                if is_symbol_adjacent(i, first_column, last_column):
                    sum += int(number)
                    print(sum)
            first_column = None
            last_column = None
            number = ""
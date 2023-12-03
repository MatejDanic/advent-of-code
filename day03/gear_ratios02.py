
schematic = []

with open("input.txt", 'r') as file:
    for line in file:
        line = line.strip()
        schematic.append([char for char in line])


gear_numbers_map = {}

def check_adjacent_gears(row, first_column, last_column, number):
    gears = []
    for i in range (row-1, row+2):
        for j in range (first_column-1, last_column+2):
            if (i >= 0 and j >= 0 and i < len(schematic) and j < len(schematic[i])):
                if schematic[i][j] == "*":
                    numbers = []
                    if gear_numbers_map.get((i, j)) is not None:
                        numbers = gear_numbers_map[(i, j)]
                    numbers.append(number)
                    gear_numbers_map[(i, j)] = numbers
    return gears

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
                check_adjacent_gears(i, first_column, last_column, number)
        # end of number
        else: 
            if number.isnumeric():
                check_adjacent_gears(i, first_column, last_column, number)
            first_column = None
            last_column = None
            number = ""

print(gear_numbers_map)

sum = 0

for gear in gear_numbers_map:
    if len(gear_numbers_map[gear]) == 2:
        print(gear, gear_numbers_map[gear])
        sum += int(gear_numbers_map[gear][0]) * int(gear_numbers_map[gear][1])
print(sum)
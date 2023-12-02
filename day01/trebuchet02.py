digit_map = {
    "zero": '0',
    "one": '1',
    "two": '2',
    "three": '3',
    "four": '4',
    "five": '5',
    "six": '6',
    "seven": '7',
    "eight": '8',
    "nine": '9'
}

def get_first_digit(line):
    word = ""
    for i in range(0, len(line)):
        word += line[i]
        for digit in digit_map:
            if word.__contains__(digit):
                return digit_map[digit]
        if line[i].isnumeric():
            return line[i]

def get_last_digit(line):
    word = ""
    for i in range(len(line)-1, -1, -1):
        word = line[i] + word
        for digit in digit_map:
            if word.__contains__(digit):
                return digit_map[digit]
        if line[i].isnumeric():
            return line[i]

sum = 0

with open("input.txt", 'r') as file:
    for line in file:
        line = line.strip()
        print(line)
        first_digit = get_first_digit(line)            
        last_digit = get_last_digit(line)
        print(first_digit, last_digit)
        sum += int(first_digit + last_digit)
        print(sum)


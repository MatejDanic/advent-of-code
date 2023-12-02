sum = 0

with open("input.txt", 'r') as file:
    for line in file:
        line = line.strip()
        print(line)
        first_digit_found = False
        for char in line:
            if char.isnumeric():
                if not first_digit_found:
                    first_digit_found = True
                    first_digit = char
                last_digit = char
        value = first_digit + last_digit
        print(first_digit, last_digit)
        sum += int(value)
        print(sum)


sum = 0

with open("example01.txt", 'r') as file:
    for line in file:
        line = line.strip()
        #print(line)
        numbers = line.split(':')[1]
        winning_numbers = numbers.split('|')[0].split(' ')
        your_numbers = numbers.split('|')[1].split(' ')
        print(winning_numbers, your_numbers)
        points = 0
        for number in winning_numbers:
            if number.isnumeric() and your_numbers.__contains__(number):
                if points == 0:
                    points = 1
                else:
                    points *= 2
        sum += points
        print(points)

print(sum)        

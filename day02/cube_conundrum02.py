sum = 0

with open("input.txt", 'r') as file:
    for line in file:
        line = line.strip()
        print(line)
        plausible = True
        maximums = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        for handful in line.split(':')[1].split(';'):
            for subset in handful.split(','):
                subset = subset.strip()
                count = int(subset.split(' ')[0])
                color = subset.split(' ')[1]
                if count > maximums[color]:
                    maximums[color] = count
            power = maximums["red"] * maximums["green"] * maximums["blue"]
        print(maximums)
        sum += power
        print(sum)

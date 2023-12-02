bag = {
    "red": 12,
    "green": 13,
    "blue": 14
}

sum = 0

with open("input.txt", 'r') as file:
    for line in file:
        line = line.strip()
        print(line)
        plausible = True
        for handful in line.split(':')[1].split(';'):
            for subset in handful.split(','):
                subset = subset.strip()
                if int(subset.split(' ')[0]) > bag[subset.split(' ')[1]]:
                    plausible = False
                    break
            if not plausible:
                break
        if plausible:
            game_id = line.split(':')[0].split(' ')[1]
            sum += int(game_id)
            print(sum)

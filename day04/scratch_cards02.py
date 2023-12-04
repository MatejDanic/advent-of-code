sum = 0

with open("input.txt", 'r') as file:
    copies = {}
    for i, card in enumerate(file):
        card = card.strip()
        numbers = card.split(':')[1]
        winning_numbers = numbers.split('|')[0].split(' ')
        your_numbers = numbers.split('|')[1].split(' ')
        matches = 0
        for number in winning_numbers:
            if number.isnumeric() and your_numbers.__contains__(number):
                matches += 1
        if matches > 0:
            for n in range(matches):
                if copies.get(i+1+n) is None:
                    copies[i+1+n] = 1
                else:
                    copies[i+1+n] = copies[i+1+n] + 1
                if copies.get(i) is not None:
                    copies[i+1+n] = copies[i+1+n] + copies[i]
        sum += 1
        if copies.get(i) is not None:
            sum += copies[i]
print(sum)
        



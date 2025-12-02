

def shift(direction, amount, starting_point):
    new_point = 0
    if direction == 'L' and amount > starting_point:
        new_point = ((starting_point - amount) % 99) + 1
    elif direction == 'L':
         new_point = (starting_point - amount) % 99
    elif direction == 'R' and (amount + starting_point) > 99:
        new_point = ((starting_point + amount) % 99) - 1
    else:
        new_point = (starting_point + amount) % 99
    return new_point
    


def main():
    point = 50
    counter = 0
    with open("input.txt") as file:
        for line in file:
            temp_list = list(line.rstrip())
            letter = temp_list[0]
            number = int(''.join(temp_list[1:]))
            point = shift(letter, number, point)
            if point == 0:
                counter+=1
    print(counter)



if __name__ == "__main__":
    main()
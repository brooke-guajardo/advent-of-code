def shift(direction, amount, starting_point):
    new_point = 0
    s_diff = starting_point - amount
    s_sum = starting_point + amount
    if direction == 'L':
        new_point = s_diff % 100
    else:
        new_point = s_sum % 100
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
            print(point)
            if point == 0:
                counter+=1
    print(f"Final password: {counter}")

if __name__ == "__main__":
    main()
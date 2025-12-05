def shift_slow(direction, amount, starting_point):
    pos = starting_point
    counter = 0
    step = -1 if direction == "L" else 1

    for _ in range(amount):
        pos = (pos + step) % 100
        if pos == 0:
            counter += 1

    return pos, counter

def shift(direction, amount, starting_point):
    counter = 0
    new_point = 0
    s_diff = starting_point - amount
    s_sum = starting_point + amount
    leftover = amount % 100
    if direction == 'L':
        new_point = s_diff % 100
        if (leftover >= starting_point) and (amount // 100) > 0 and starting_point !=0 and leftover != 0: # does this fully wrap and partially wrap (u cant start at 0 and partially wrap)
            counter += 1 + (amount//100)
        elif leftover <= starting_point and (amount // 100) > 0: # maybe only fully wraps
            counter += (amount//100)
        elif (leftover >= starting_point) and (amount // 100) <= 0 and starting_point != 0 and leftover != 0: # maybe only partially wraps
            counter+=1
        else: # no wraps at all
            pass
    else: # "R"
        new_point = s_sum % 100
        if (starting_point + leftover) > 99 and (amount // 100) > 0: # does this fully wrap and partially wrap
            counter += 1 + (amount//100)
        elif (starting_point + leftover) < 99 and (amount // 100) > 0: # maybe only fully wraps
            counter += (amount//100)
        elif (starting_point + leftover) > 99 and (amount // 100) <= 0: # maybe only partially wraps
            counter+=1
        else: # no wraps at all
            pass  
        
    return new_point, counter

def main():
    point = 50
    counter = 0
    with open("input.txt") as file:
        for line in file:
            temp_list = list(line.rstrip())
            letter = temp_list[0]
            number = int(''.join(temp_list[1:]))
            point, cnt = shift_slow(letter, number, point)
            counter = cnt + counter
            # print(f"Direction: {letter} Amount: {number} Point End: {point} Count: {counter}")
    print(f"Final password: {counter}")

if __name__ == "__main__":
    main()
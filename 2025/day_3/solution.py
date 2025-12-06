def bank(bank_batteries: str):
    all_batts = list(bank_batteries.rstrip())
    
    batt_count = len(all_batts)
    diff = batt_count - 12
    final_batt = [0] * 12
    start = 0
    position = 0
    # print(bank_batteries)
    # print(all_batts)

    # I can only search for the first number 1 + diff positions before locking in
    while position < 12:
        temp = start
        for index in range(start, batt_count - (len(final_batt) - (position + 1))):
            #print(f"Compare {final_batt[position]} vs {all_batts[index]} for position: {position}, index at {index}, start at {start}")
            if final_batt[position] < int(all_batts[index]):
                final_batt[position] = int(all_batts[index])
                temp = index
        position+=1
        # print(f"Position: {position}")
        start = temp + 1

    return int(''.join([str(num) for num in final_batt]))

def main():
    joltage = 0
    with open("input.txt") as file:
        for line in file:
            # print(line)
            # print(bank(line))
            joltage = bank(line) + joltage
    print(joltage)
    return joltage

if __name__ == "__main__":
    main()
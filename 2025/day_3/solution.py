def bank(bank_batteries: str):
    all_batts = list(bank_batteries.rstrip())
    batt_1 = 0
    batt_2 = 0
    index_1 = 0
    index_2 = 0

    # first search, needs to get number's index
    for i in range(len(all_batts)-1):
        if int(all_batts[i]) > int(batt_1):
            batt_1 = int(all_batts[i])
            index_1 = i
           
    for j in range(index_1 + 1, len(all_batts)):
        if int(all_batts[j]) > int(batt_2):
            batt_2 = int(all_batts[j])
    # else:
    #     print("bork")
    #     for j in range(0,len(all_batts) - 1):
    #         if int(all_batts[j]) > int(batt_2):
    #             batt_2 = int(all_batts[j])
    #             index_2 = j
    #     temp = (batt_1 * 10) + batt_2

    return (batt_1 * 10) + batt_2

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
total = 0
f = open("2022_04_input.txt", "r")
for line in f:
    print(line)
    ranges        = line.split(',')
    ranges[1]     = ranges[1].strip()
    range_one     = ranges[0].split('-')
    range_two     = ranges[1].split('-')
    range_set_one = [ num for num in range(int(range_one[0]),int(range_one[1]) + 1,1) ]
    range_set_two = [ num for num in range(int(range_two[0]),int(range_two[1]) + 1,1) ]
    #print(range_set_one)
    #print(range_set_two)
    if set(range_set_one) & set(range_set_two):
        print("These overlap")
        total = total + 1

print(total)


# 1 A X rock
# 2 B Y paper
# 3 C Z scissors
# 0 lose, 3 tie, 6 win
def winner(ply1, ply2):
    if ply1 == 'A':
        if ply2 == 'X':
            return 4
        elif ply2 == 'Y':
            return 8
        else:
            return 3
    elif ply1 == 'B':
        if ply2 == 'X':
            return 1
        elif ply2 == 'Y':
            return 5
        else:
            return 9
    else:
        if ply2 == 'X':
            return 7
        elif ply2 == 'Y':
            return 2
        else:
            return 6

total = 0
f = open("2022_02_input.txt", "r")
for line in f:
    my_arr = line.split()
    print(my_arr)
    print(winner(my_arr[0], my_arr[1]))
    total = winner(my_arr[0], my_arr[1]) + total

print(total)

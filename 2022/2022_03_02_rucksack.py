from itertools import islice

def priority_val(letter):
    s = 'abcdefghijklmnopqrstuvwxyz'
    S = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if letter in s:
        return s.find(letter) + 1
    elif letter in S:
        return S.find(letter) + 27
    else:
        return 0

total = 0
with open("2022_03_input.txt", "r") as f:
    while True:
        three_ruck_sacks = list(islice(f,3))
        if not three_ruck_sacks:
            break
        print(three_ruck_sacks)
        badge = str(set(three_ruck_sacks[0].strip()) & set(three_ruck_sacks[1].strip()) & set(three_ruck_sacks[2].strip()))
        print(badge[2])
        total = total + priority_val(badge[2])

print(total)

def priority_val(letter):
    s = 'abcdefghijklmnopqrstuvwxyz'
    S = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if letter in s:
        print(f"Sum: {s.find(letter) + 1}")
        return s.find(letter) + 1
    elif letter in S:
        print(f"Sum: {S.find(letter) + 27}")
        return S.find(letter) + 27
    else:
        return 0

total = 0
f = open("2022_03_input.txt", "r")
for line in f:
    print(line)
    rs1 = slice( 0, (len(line) - 1)//2, 1)
    rs2 = slice( (len(line) - 1)//2, len(line) - 1, 1)
#    print(set(line[rs1]) & set(line[rs2]) )
    letter = str(set(line[rs1]) & set(line[rs2]))
    print(letter[2])
#    print(priority_val(letter[2]))
    total = total + priority_val(letter[2])

print(total)

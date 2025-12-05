

def pal_check(seq: str):
    summ = 0
    rng = seq.split('-')
    start = int(rng[0])
    finish = int(rng[1])
    seq_arr = []
    for num in range(start, finish+1):
        seq_arr.append(num)
    for check in seq_arr:
        s = str(check)
        ln = len(s)
        if ln % 2 != 0:
            continue
        if ln <= 2:
            if s == s[::-1]:
                summ+=check
                continue
            else:
                continue
        if s[0:int(ln/2):] == s[int(ln/2):ln:]:
            summ+=check
    return summ

def main():
    summ = 0
    with open("input.txt") as file:
        line = file.read()
        seq = line.split(',')
        for s in seq:
            summ += pal_check(s)
    print(summ)
            


if __name__ == "__main__":
    main()
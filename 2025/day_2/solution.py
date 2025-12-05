from itertools import groupby
from functools import reduce

def factors(n):
    full_set = set(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if not n % i)))
    return full_set.difference({1, n})

def get_range(seq: str):
    rng = seq.split('-')
    start = int(rng[0])
    finish = int(rng[1])
    seq_arr = []
    for num in range(start, finish+1):
        seq_arr.append(num)
    return seq_arr
    
def all_equal(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False)

def slice_n_diced(num: str):
    diced = []
    ln = len(num)
    fctrs = factors(ln)
    if fctrs == {}:
        return False
    # print(f"Factors: {fctrs} Number: {num}")
    for sub_ln in fctrs:
        for i in range(0,ln,sub_ln):
            diced.append(num[i:i+sub_ln])
        if diced == []:
            return False
        if all_equal(diced):
            return True
        diced = []
    return False

def check(seq: str):
    summ = 0
    seq_arr = get_range(seq)
    check_arr = []
    for check in seq_arr:
        s = str(check)
        ln = len(s)
        # if all repeating numbers
        if ln < 2:
            continue
        if ln == s.count(s[0:1:]):
            summ+=check
            check_arr.append(check)
            # print(f"Invalid ID Meow: {s}")
            continue
        if ln == 2:
            if s == s[::-1]:
                summ+=check
                check_arr.append(check)
                # print(f"Invalid ID Bork: {s}")
                continue
            else:
                continue
        if s[0:int(ln/2):] == s[int(ln/2):ln:]:
            summ+=check
            check_arr.append(check)
            # print(f"Invalid ID Moo: {s}")
            continue
        if slice_n_diced(s):
            summ+=check
            check_arr.append(check)
            # print(f"Invalid ID Quack: {s}")
            continue            
    # print(f"Sequence: {seq}\nInvalid IDs: {check_arr}")
    return summ

def main():
    summ = 0
    with open("input.txt") as file:
        line = file.read()
        seq = line.split(',')
        for s in seq:
            summ += check(s)
    print(summ)
    return summ
            
# 54446379166 - too high

if __name__ == "__main__":
    main()
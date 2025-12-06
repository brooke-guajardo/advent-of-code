def get_range(seq: str):
    rng = seq.split('-')
    start = int(rng[0])
    finish = int(rng[1])
    return [start,finish]

def check_ingredients(ids: list):
    all_ingredients_count = 0
    # if 1 - [] 2 - ()
    # [ ( ] ) - overlap 1[ < 2( < 1] < 2)
    # ( [ ) ] - overlap 2( < 1[ < 2) < 1]
    # [ ( ) ] - overlap
    # ( ) [ ] - just count
    # [ ] ( ) - just count
    for id_range_1 in ids:
        for id_range_2 in ids:
            if id_range_1 != id_range_2:
                if id_range_1[0] <= id_range_2[0] <= id_range_1[1] <= id_range_2[1]:
                    # print(f"Overlap 1: Range One: {id_range_1}, Range Two: {id_range_2}")
                    id_range_1[1] = id_range_2[1]
                    id_range_2[0] = id_range_1[0]
                    continue
                if id_range_2[0] <= id_range_1[0] <= id_range_2[1] <= id_range_1[1]:
                    # print(f"Overlap 2: Range One: {id_range_1}, Range Two: {id_range_2}")
                    id_range_1[0] = id_range_2[0]
                    id_range_2[1] = id_range_1[1]
                    continue
                if id_range_1[0] <= id_range_2[0] <= id_range_2[1] <= id_range_1[1]:
                    # print(f"Overlap 3: Range One: {id_range_1}, Range Two: {id_range_2}")
                    id_range_2[0] = id_range_1[0]
                    id_range_2[1] = id_range_1[1]
                    continue

    set_of_ids = [list(x) for x in set(tuple(x) for x in ids)]
    for ranges in set_of_ids:
        all_ingredients_count+= ranges[1] - ranges[0] + 1
    print(all_ingredients_count)
    return all_ingredients_count

def get_chonker(arr: list):
    all_nums_in_ranges = []
    for rng in arr:
        all_nums_in_ranges.append(get_range(rng))
    return all_nums_in_ranges

def main():
    ingredient_ids = []
    with open("input.txt") as file:
        for line in file:
            if '-' in line:
                ingredient_ids.append(line.rstrip())
                continue
            if line.rstrip() == '':
                break
            # ingredients.append(line.rstrip())
    # print(ingredient_ids)
    chonker = get_chonker(ingredient_ids)
    return check_ingredients(chonker)
    

if __name__ == "__main__":
    main()
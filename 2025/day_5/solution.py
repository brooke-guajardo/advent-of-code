def get_range(seq: str):
    rng = seq.split('-')
    start = int(rng[0])
    finish = int(rng[1])
    return [start,finish]

def check_ingredients(ids: list, ingredients: list):
    unspoiled = 0
    for food in ingredients:
        for id_range in ids:
            if id_range[0] <= int(food) <= id_range[1]:
                unspoiled+=1
                break
    print(unspoiled)
    return unspoiled

def get_chonker(arr: list):
    all_nums_in_ranges = []
    for rng in arr:
        all_nums_in_ranges.append(get_range(rng))
    return all_nums_in_ranges

def main():
    ingredient_ids = []
    ingredients = []
    with open("input.txt") as file:
        for line in file:
            if '-' in line:
                ingredient_ids.append(line.rstrip())
                continue
            if line.rstrip() == '':
                continue
            ingredients.append(line.rstrip())
    chonker = get_chonker(ingredient_ids)
    return check_ingredients(chonker, ingredients)
    

if __name__ == "__main__":
    main()
def remove_rolls(rolls_before: list, coords_to_remove: list, forklist_count: int):
    for coords in coords_to_remove:
        rolls_before[coords[0]][coords[1]] = '.'
    
    return pain(rolls_before, forklist_count)
    
    

def pain(arr: list, forklift_count: int):
    columns = len(arr[0])
    rows = len(arr)
    coords = []
    for i in range(0,columns):
        for j in range(0,rows):
            paper_count = 0
            if arr[i][j] == '@':
                ### if row and colmun is the first and the last, i.e. 4 corners
                if (i == 0 and j == 0) or (i == columns - 1 and j == 0) or (i == 0 and j == rows - 1) or (i == columns - 1 and j == rows - 1):
                    forklift_count+=1
                    coords.append((i,j))
                    # print(f"Corner: {i},{j}")
                    continue
                ### if column is first or the last
                elif j == 0 or j == columns - 1:
                    # check 5 positions
                    # first up n down
                    if arr[i-1][j] == '@': # up
                        paper_count+=1
                    if arr[i+1][j] == '@': # down
                        paper_count+=1

                    # check L or R depending on j value
                    if j == 0: # right
                        if arr[i-1][j+1] == '@': 
                            paper_count+=1
                        if arr[i][j+1] == '@':
                            paper_count+=1
                        if arr[i+1][j+1] == '@':
                            paper_count+=1
                    else: # left
                        if arr[i-1][j-1] == '@':
                            paper_count+=1
                        if arr[i][j-1] == '@':
                            paper_count+=1
                        if arr[i+1][j-1] == '@':
                            paper_count+=1
                    if paper_count < 4:
                        forklift_count+=1
                        coords.append((i,j))
                        # print(f"Coordinates: {i},{j}")
                        continue
                ### if row is the first or the last
                elif i == 0 or i == rows - 1:
                    # need to check 5 positions
                    # first L and R
                    if arr[i][j-1] == '@':
                        paper_count+=1
                    if arr[i][j+1] == '@':
                        paper_count+=1
                    # check above or below depending on i value
                    if i == 0: # below
                        if arr[i+1][j-1] == '@':
                            paper_count+=1
                        if arr[i+1][j] == '@':
                            paper_count+=1
                        if arr[i+1][j+1] == '@':
                            paper_count+=1
                    else: # above
                        if arr[i-1][j-1] == '@':
                            paper_count+=1
                        if arr[i-1][j] == '@':
                            paper_count+=1
                        if arr[i-1][j+1] == '@':
                            paper_count+=1
                    if paper_count < 4:
                        forklift_count+=1
                        coords.append((i,j))
                        # print(f"Coordinates: {i},{j}")
                        continue
                else:
                    # 8 coordinates relative to i,j
                    # i-1, j-1  i-1,j  i-1,j+1
                    # i,   j-1 sounrce i,  j+1
                    # i+1, j-1  i+1,j  i+1,j+1
                    # above
                    if arr[i-1][j-1] == '@':
                            paper_count+=1
                    if arr[i-1][j] == '@':
                            paper_count+=1
                    if arr[i-1][j+1] == '@':
                            paper_count+=1
                    # below
                    if arr[i+1][j-1] == '@':
                        paper_count+=1
                    if arr[i+1][j] == '@':
                        paper_count+=1
                    if arr[i+1][j+1] == '@':
                        paper_count+=1
                    # L and R
                    if arr[i][j-1] == '@':
                        paper_count+=1
                    if arr[i][j+1] == '@':
                        paper_count+=1
                    if paper_count < 4:
                        forklift_count+=1
                        coords.append((i,j))
                        # print(f"Coordinates: {i},{j}")
                        continue
    if coords != []:
        return remove_rolls(arr, coords, forklift_count)
    else:
        return forklift_count


def main():
    big_boi_arr = []
    with open("input.txt") as file:
        for line in file:
            big_boi_arr.append(list(line.rstrip()))
    num = pain(big_boi_arr,0)
    print(num)
    return num
    

if __name__ == "__main__":
    main()
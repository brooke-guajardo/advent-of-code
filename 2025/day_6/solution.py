def rolly_polly_math(arr: list):
    columns = len(arr[0])
    rows = len(arr)
    # print(arr)
    print(f"Rows {rows}, Columns {columns}")
    grand_total = 0
    for i in range(0,columns):
        col = []
        for j in range(0,rows):
            col.append(arr[j][i])
        print(col)
        if col[rows-1] == "*":
            col_total_value = 1
            for value in col[:rows-1:]:
                col_total_value *= int(value)
            grand_total += col_total_value
        else: 
            for value in col[:rows-1:]:
                grand_total += int(value)
    print(grand_total)
    return grand_total

def main():
    big_boi_arr = []
    with open("input.txt") as file:
        for line in file:
            big_boi_arr.append(line.strip().split())
    rolly_polly_math(big_boi_arr)
    
if __name__ == "__main__":
    main()
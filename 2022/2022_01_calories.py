f = open("2022_01_input.txt", "r")

my_string = f.read()
my_arr = my_string.split('\n')

total = 0
curr_total = 0
for num in my_arr:
    if num != '':
        curr_total = curr_total + int(num)
        #print(f"This is current number: {num}")
    else:
        if curr_total > total:
            total = curr_total
            #print(f"New Total Largest Calories: {total}")
        curr_total = 0

print(total)

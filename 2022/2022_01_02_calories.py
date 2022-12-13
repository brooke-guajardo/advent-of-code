f = open("2022_01_input.txt", "r")

my_string = f.read()
my_arr = my_string.split('\n')

each_elf   = []
curr_total = 0
for num in my_arr:
    if num != '':
        curr_total = curr_total + int(num)
        #print(f"This is current number: {num}")
    else:
        each_elf.append(curr_total)
        curr_total = 0

each_elf.sort(reverse=True)
print(each_elf[0]+ each_elf[1] + each_elf[2])

import re

f  = open("2022_07_input.test", "r")
ff = open("2022_07_input.test", "r")
my_string = ff.read()
my_arr = my_string.split('\n')

print(my_arr)
dict_of_dirs = {}

for line in f:
    if "$" in line and "cd" in line and "." not in line:
        print(line)
        #dict_of_dirs[line.strip().lstrip("$ ")] = [ x for x in my_arr[my_arr.index(line.strip()):] ]
        #dict_of_dirs[line.strip().lstrip("$ ")] = list(next(iter(())) if "$ cd" in ele else ele for ele in my_arr[my_arr.index(line.strip())+1:] if re.match('[^0-9]+', ele))
        dict_of_dirs[line.strip().lstrip("$ ")] = list(next(iter(())) if "$ cd" in ele else ele for ele in my_arr[my_arr.index(line.strip())+1:] if False)
    if re.match('^[0-9]+', line):
        print(f"Number lines: {line}")

for element in dict_of_dirs:
    print(element)
    print(dict_of_dirs[element])


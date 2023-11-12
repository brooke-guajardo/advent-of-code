from collections import defaultdict

#f  = open("2022_07_input.test", "r")
file      = open("2022_07_input.test", "r")
my_string = file.read()
my_arr    = my_string.split('\n')

#print(my_arr)

def build_dir(big_arr, it):
    small_arr = big_arr[it:len(big_arr)]
    new_arr   = []
    for element in small_arr:
        #print(f"{element}") 
        if "cd" in element or element in small_arr[-1]:
            return new_arr
        elif "$ ls" not in element and "dir" not in element:
            new_arr.append(element)

#print(build_dir(my_arr,0))

my_dict = defaultdict(list)
dict_iter=0
itr=0
for line in my_arr:
    itr=itr+1
    print(f"Line {line}")
    #if "$ cd" in line and "$ cd .." not in line:
    if "$ ls" in line:
        my_dict[dict_iter].append(build_dir(my_arr, itr))
        dict_iter=dict_iter+1

print(my_dict)

#initial_arr = [1,2,3,4,5]
#print(f"What to slice this array at 2: {initial_arr}")
#new_arr = build_dir(initial_arr, 2)
#print(f"New array: {new_arr}")

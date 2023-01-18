f = open("2022_06_input.txt", "r")
my_string = f.read()


my_list     = []
my_list[:0] = my_string


marker = 14
overlap = marker - 1


list_of_markers = [my_list[i:i+marker] for i in range(0, len(my_list),marker-overlap)]

for message in list_of_markers:
    if len(set(message)) == marker:
        print(f"no dupes!")
        print(message)
        print(f"Index value {list_of_markers.index(message) + overlap + 1}")
        break


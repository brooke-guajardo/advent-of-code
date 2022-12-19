# initial box stacked
s1 = ['S','L','W']
s2 = ['J','T','N','Q']
s3 = ['S','C','H','F','J']
s4 = ['T','R','M','W','N','G','B']
s5 = ['T','R','L','S','D','H','Q','B']
s6 = ['M','J','B','V','F','H','R','L']
s7 = ['D','W','R','N','J','M']
s8 = ['B','Z','T','F','H','N','D','J']
s9 = ['H','L','Q','N','B','F','T']

#s1 = ['W','L','S']
#s2 = ['Q','N','T','J']
#s3 = ['J','F','H','C','S']
#s4 = ['B','G','N','W','M','R','T']
#s5 = ['B','Q','H','D','S','L','R','T']
#s6 = ['L','R','H','F','V','B','J','M']
#s7 = ['M','J','N','R','W','D']
#s8 = ['J','D','N','H','F','T','Z','B']
#s9 = ['T','F','B','N','Q','L','H']

class Stack:
    def __init__(self, stack_num):
        #self.stack_num = [ele for ele in stack_num]
        self.stack_num = stack_num

    def remove_box(self, num):
        # use pop to remove box and return the value of the box removed
        moving_boxes = []
        bad_rev = len(self.stack_num)
        for box in range(0,num):
            moving_boxes.append(self.stack_num.pop(bad_rev - 1 - box))
        return moving_boxes

    def get_stack(self):
        # debug
        return self.stack_num

    def add_box(self, new_box):
        # add box
        for box in new_box:
            self.stack_num.append(box)

stack_one   = Stack(s1)
stack_two   = Stack(s2)
stack_three = Stack(s3)
stack_four  = Stack(s4)
stack_five  = Stack(s5)
stack_six   = Stack(s6)
stack_seven = Stack(s7)
stack_eight = Stack(s8)
stack_nine  = Stack(s9)

box_dict    = {1:stack_one, 2:stack_two, 3:stack_three, 4:stack_four, 5:stack_five, 6:stack_six, 7:stack_seven, 8:stack_eight, 9:stack_nine}

f         = open("2022_05_moves_input.txt", "r")
my_string = f.read()
my_arr    = my_string.split('\n')
for steps in my_arr:
    if steps != '':
        crane = steps.split(' ')
        print(f"This many: {crane[1]}, from {crane[3]} to {crane[5]}")
        print(box_dict[int(crane[3])].get_stack())
        print(box_dict[int(crane[5])].get_stack())
        crane_claw = box_dict[int(crane[3])].remove_box(int(crane[1]))
        crane_claw.reverse()
        print(f"Contents of crane claw: {crane_claw}")
        print(box_dict[int(crane[3])].get_stack())
        box_dict[int(crane[5])].add_box(crane_claw)
        print(box_dict[int(crane[5])].get_stack())

print(f"meow")

for num in range(1,10,1):
    print(box_dict[num].get_stack())


# height = int(input('what is your height in cm?\n'))
#
# if height > 120:
#     print("you have a normal height")
# else:
#     print('sorry reduce your height')

# import random
#
# random_side = random.randint(0, 1)
# if random_side == 1:
#     print('Head')
# else:
#     print('Hail')

row1 = [" "," "," "]
row2 = [" "," "," "]
row3 = [" "," "," "]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("where do you want to put the treasure?")

horizonal = int(position[0])
vertical = int(position[1])

selected_row = map[vertical - 1]
selected_row[horizonal - 1] = "x"

print(f"{row1}\n{row2}\n{row3}")









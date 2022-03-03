import sys
import time

width = 120
height = 20
canvas = []

for i in range(height):
    temp = []
    for k in range(width):
        temp.append(0)
    canvas.append(temp)

empty_canvas = canvas.copy()

# for i in range(height):
#     for k in range(width):
#         if(i == 0 or i == (height - 1) or k == 0 or k == (width - 1)):
#             canvas[i][k] = 1

def build(tab):
    temp = []
    for i in range(height):
        line = ""
        for k in range(width):
            if(tab[i][k]):
                line += "██"
            else:
                line += "  "
        temp.append(line + "\n")

    return temp


index = 0
while(1):
    # count = 5
    # while(count >= 0):
    #     sys.stdout.write("\n")
    #     count -= 1
    canvas = []
    for i in range(height):
        temp = []
        for k in range(width):
            temp.append(0)
        canvas.append(temp)
    canvas[5][index] = 1

    to_print = build(canvas)

    for line in to_print:
        print(line)
    time.sleep(0.05)
    index += 1

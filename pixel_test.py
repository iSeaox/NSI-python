import sys
import time

width = 80
height = 40
canvas = []

for i in range(height):
    temp = []
    for k in range(width):
        temp.append(0)
    canvas.append(temp)

empty_canvas = canvas.copy()

for i in range(height):
    for k in range(width):
        if(i == 0 or i == (height - 1) or k == 0 or k == (width - 1)):
            canvas[i][k] = 1

def build(tab):
    temp = []
    for i in range(height):
        line = ""
        for k in range(width):
            if(tab[i][k]):
                line += "██"
            else:
                line += "  "
        temp.append(line)

    return temp



to_print = build(canvas)
for line in to_print:
    sys.stdout.write(line+"\n")



while(1):
    # count = 5
    # while(count >= 0):
    #     sys.stdout.write("\n")
    #     count -= 1



    to_print = build(canvas)

    for line in to_print:
        sys.stdout.write(line + "\n")
    time.sleep(0.2)

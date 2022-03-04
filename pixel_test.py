import sys
import time
import keyboard

running = ["""
      ██
    ██████
  ██  ██  ████
      ██
      ██
    ██  ██
████      ██
            ██
""", """
      ██
    ██████
  ██  ██  ████
      ██
      ██
    ██  ██
████      ██
          ██
""", """
      ██
    ██████
  ██  ██  ████
  ██  ██
      ██
      ████
    ██████
        ██
""", """
      ██
    ██████
  ██  ██  ████
  ██  ██
      ██
    ██  ████
  ██        ██
  ██
""", """
      ██
    ██████
  ██  ██  ████
  ██  ██
      ██
    ██  ████
████        ██

"""]
width = 120
height = 40
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

def blit(can, sprite, x, y):
    splited_sprite = sprite.split("\n")
    for i in range(len(splited_sprite)):
        j = 0
        while(j < len(splited_sprite[i])):
            if(splited_sprite[i][j:(j+2)] == "██"):
                canvas[y + i][x + (j // 2)] = 1
            j += 2


global x
global y
x = 10
y = 10

def change():
    global y
    y -= 8

keyboard.add_hotkey('esc', lambda: change())

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

    if(index % len(running) == 0):
        y = 10

    blit(canvas, running[index % len(running)], x, y)
    to_print = build(canvas)

    for line in to_print:
        print(line, end="")
    time.sleep(0.2)
    index += 1

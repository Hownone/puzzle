import random

SIZE = 360
WIDTH = SIZE * 3
HEIGHT = SIZE *3
Lastpic = Actor("9")
Lastpic.left = 2 * SIZE
Lastpic.top = 2 * SIZE
Flag = False

pics = []

for i in range(1,9):
    pic = Actor(str(i))
    pic.index = i - 1
    pics.append(pic)


random.shuffle(pics)

for i in range(8):
    pics[i].left = i % 3 * SIZE
    pics[i].top = i // 3 * SIZE

def get_pic(grid_x,grid_y):
    for pic in pics:
        if pic.x // SIZE == grid_x and pic.y // SIZE == grid_y:
            return pic
    return None

def on_mouse_down(pos):
    if Flag:
        return
    grid_x = pos[0] // SIZE
    grid_y = pos[1] // SIZE
    thispic = get_pic(grid_x,grid_y)
    if (thispic == None):
        return
    if grid_y > 0 and get_pic(grid_x,grid_y - 1) == None:
        thispic.y -= SIZE
        return
    if grid_y < 2 and get_pic(grid_x,grid_y + 1) == None:
        thispic.y += SIZE
        return
    if grid_x > 0 and get_pic(grid_x - 1,grid_y) == None:
        thispic.x -= SIZE
        return
    if grid_x < 2 and get_pic(grid_x + 1,grid_y) == None:
        thispic.x += SIZE
        return

def update():
    global Flag
    if Flag:
        return
    for i in range(8):
        pic = get_pic(i % 3,i // 3)
        if (pic == None or pic.index != i):
            return
    Flag = True
    sounds.win.play()




def draw():
    screen.fill((255,255,255))
    for pic in pics:
        pic.draw()
    if Flag:
        Lastpic.draw()
        screen.draw.text("Congratulation！", center=(WIDTH // 2, HEIGHT // 2),
                        fontsize=100, color="red")



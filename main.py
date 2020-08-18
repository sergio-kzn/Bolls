from tkinter import *
from random import randrange as rnd, choice
import time
root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg='white')
label_score = Label(bg='gray', fg='white', text='Очки: 0', width=800)
canv.pack(fill=BOTH, expand=1)
label_score.pack()

colors = ['red', 'orange', 'yellow', 'green', 'blue']
score = 0
routes = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
route = choice(routes)
speed_animation = 10
step_animation = 2


def move_N(): # шарик двигается вверх
    if canv.coords(oval)[1] < 1:
        global route
        route = choice(routes)
        canv.itemconfig(oval, fill=choice(colors))
    else:
        canv.move(oval, 0, -step_animation)


def move_NE(): # шарик двигается вверх вправо
    if canv.coords(oval)[1] < 1 or canv.coords(oval)[2] > 799:
        global route
        route = choice(routes)
        canv.itemconfig(oval, fill=choice(colors))
    else:
        canv.move(oval, step_animation, -step_animation)


def move_E(): # шарик двигается вправо
    if canv.coords(oval)[2] > 799:
        global route
        route = choice(routes)
        canv.itemconfig(oval, fill=choice(colors))
    else:
        canv.move(oval, step_animation, 0)


def move_SE(): # шарик двигается вниз вправо
    if canv.coords(oval)[3] > 599 or canv.coords(oval)[2] > 799:
        global route
        route = choice(routes)
        canv.itemconfig(oval, fill=choice(colors))
    else:
        canv.move(oval, step_animation, step_animation)


def move_S(): # шарик двигается вниз
    if canv.coords(oval)[3] > 599:
        global route
        route = choice(routes)
        canv.itemconfig(oval, fill=choice(colors))
    else:
        canv.move(oval, 0, step_animation)


def move_SW(): # шарик двигается вниз влево
    if canv.coords(oval)[3] > 599 or canv.coords(oval)[0] < 1:
        global route
        route = choice(routes)
        canv.itemconfig(oval, fill=choice(colors))
    else:
        canv.move(oval, -step_animation, step_animation)


def move_W(): # шарик двигается влево
    if canv.coords(oval)[0] < 1:
        global route
        route = choice(routes)
        canv.itemconfig(oval, fill=choice(colors))
    else:
        canv.move(oval, -step_animation, 0)


def move_NW(): # шарик двигается вверх влево
    if canv.coords(oval)[1] < 1 or canv.coords(oval)[0] < 1:
        global route
        route = choice(routes)
        canv.itemconfig(oval, fill=choice(colors))
    else:
        canv.move(oval, -step_animation, -step_animation)


def create_boll():    # создаем шарик случайного цвета, размера и позиции
    global x, y, r, oval
    canv.delete(ALL)
    x = rnd(100, 700)
    y = rnd(100, 500)
    r = rnd(30, 50)
    oval = canv.create_oval(x-r, y-r, x+r, y+r, fill=choice(colors), width=0)


def move_ball():
    # теперь шарик надо заставить двигаться

    if route == "N":
        move_N()
    elif route == 'NE':
        move_NE()
    elif route == 'E':
        move_E()
    elif route == 'SE':
        move_SE()
    elif route == 'S':
        move_S()
    elif route == 'SW':
        move_SW()
    elif route == 'W':
        move_W()
    elif route == 'NW':
        move_NW()

    root.after(speed_animation, move_ball)


def click(event):
    # вычисляем расстояние между двумя точками
    x = canv.coords(oval)[2] - r
    y = canv.coords(oval)[3] - r
    rasstoyanie = ((x - event.x)**2 + (y - event.y)**2)**0.5

    if rasstoyanie <= r:
        global score, route
        score += 1
        label_score['text'] = 'Очки: ' + str(score)
        canv.delete(oval)
        route = choice(routes)
        create_boll()


create_boll()
move_ball()

canv.bind('<Button-1>', click)
mainloop()


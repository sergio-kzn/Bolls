from random import randrange as rnd, choice
from tkinter import *

routes = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
colors = ['red', 'orange', 'yellow', 'green', 'blue']
score = 0
speed_animation = 10


class Boll:
    def __init__(self):
        self.step_animation = 2
        self.x = rnd(100, 700)
        self.y = rnd(100, 500)
        self.r = rnd(30, 50)
        self.oval = canvas.create_oval(self.x - self.r, self.y - self.r,
                                  self.x + self.r, self.y + self.r,
                                  fill=choice(colors))

    def move_boll(self, route):
        color = choice(colors)
        if route == 'N':  # шарик двигается вверх
            if canvas.coords(self.oval)[1] < 1:
                canvas.itemconfig(self.oval, fill=color)
            else:
                canvas.move(self.oval, 0, -self.step_animation)

        elif route == 'NE':  # шарик двигается вверх вправо
            if canvas.coords(self.oval)[1] < 1 or canvas.coords(self.oval)[2] > 799:
                canvas.itemconfig(self.oval, fill=color)
            else:
                canvas.move(self.oval, self.step_animation, -self.step_animation)

        elif route == 'E':  # шарик двигается вправо
            if canvas.coords(self.oval)[2] > 799:
                canvas.itemconfig(self.oval, fill=color)
            else:
                canvas.move(self.oval, self.step_animation, 0)

        elif route == 'SE':  # шарик двигается вниз вправо
            if canvas.coords(self.oval)[3] > 599 or canvas.coords(self.oval)[2] > 799:
                canvas.itemconfig(self.oval, fill=color)
            else:
                canvas.move(self.oval, self.step_animation, self.step_animation)

        elif route == 'S':  # шарик двигается вниз
            if canvas.coords(self.oval)[3] > 599:
                canvas.itemconfig(self.oval, fill=color)
            else:
                canvas.move(self.oval, 0, self.step_animation)

        elif route == 'SW':  # шарик двигается вниз влево
            if canvas.coords(self.oval)[3] > 599 or canvas.coords(self.oval)[0] < 1:
                canvas.itemconfig(self.oval, fill=color)
            else:
                canvas.move(self.oval, -self.step_animation, self.step_animation)

        elif route == 'W':  # шарик двигается влево
            if canvas.coords(self.oval)[0] < 1:
                canvas.itemconfig(self.oval, fill=color)
            else:
                canvas.move(self.oval, -self.step_animation, 0)

        elif route == 'NW':  # шарик двигается вверх влево
            if canvas.coords(self.oval)[1] < 1 or canvas.coords(self.oval)[0] < 1:
                canvas.itemconfig(self.oval, fill=color)
            else:
                canvas.move(self.oval, -self.step_animation, -self.step_animation)


def tick():
    # теперь шарик надо заставить двигаться
    route = choice(routes)
    ball1.move_boll(route)

    root.after(speed_animation, tick)


def click(event):
    # вычисляем расстояние между двумя точками
    x = canvas.coords(oval)[2] - r
    y = canvas.coords(oval)[3] - r
    rasstoyanie = ((x - event.x) ** 2 + (y - event.y) ** 2) ** 0.5

    if rasstoyanie <= r:
        global score, route
        score += 1
        label_score['text'] = 'Очки: ' + str(score)
        canvas.delete(oval)
        # route = choice(routes)
        # create_boll()


def main():
    global root, canvas, ball1

    root = Tk()
    root.geometry('800x600')
    canvas = Canvas(root, bg='white')
    label_score = Label(bg='gray', fg='white', text='Очки: 0', width=800)
    canvas.pack(fill=BOTH, expand=1)
    label_score.pack()

    canvas.bind('<Button-1>', click)

    ball1 = Boll()
    tick()
    root.mainloop()


if __name__ == '__main__':
    main()


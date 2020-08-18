from random import randrange as rnd, choice
from tkinter import *

routes = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
route = choice(routes)
colors = ['red', 'orange', 'yellow', 'green', 'blue']
score = 0
speed_animation = 20


class Boll:
    def __init__(self):
        self.step_animation = 1
        self.r = rnd(30, 50)
        self.x = rnd(self.r, 700)
        self.y = rnd(self.r, 500)
        self.oval = canvas.create_oval(self.x - self.r, self.y - self.r,
                                       self.x + self.r, self.y + self.r,
                                       fill=choice(colors))

    def change_route(self):  # меняем направление движения
        global route
        if (canvas.coords(self.oval)[1] < 1
                or canvas.coords(self.oval)[0] < 1
                or canvas.coords(self.oval)[3] > 599
                or canvas.coords(self.oval)[2] > 799):
            route = choice(routes)
            color = choice(colors)
            canvas.itemconfig(self.oval, fill=color)

    def move_boll(self):  # направляем шарик в нужную сторону
        if route == 'N':  # шарик двигается вверх
            canvas.move(self.oval, 0, -self.step_animation)

        elif route == 'NE':  # шарик двигается вверх вправо
            canvas.move(self.oval, self.step_animation, -self.step_animation)

        elif route == 'E':  # шарик двигается вправо
            canvas.move(self.oval, self.step_animation, 0)

        elif route == 'SE':  # шарик двигается вниз вправо
            canvas.move(self.oval, self.step_animation, self.step_animation)

        elif route == 'S':  # шарик двигается вниз
            canvas.move(self.oval, 0, self.step_animation)

        elif route == 'SW':  # шарик двигается вниз влево
            canvas.move(self.oval, -self.step_animation, self.step_animation)

        elif route == 'W':  # шарик двигается влево
            canvas.move(self.oval, -self.step_animation, 0)

        elif route == 'NW':  # шарик двигается вверх влево
            canvas.move(self.oval, -self.step_animation, -self.step_animation)


def tick():
    ball1.change_route()
    ball1.move_boll()

    root.after(speed_animation, tick)


def click(event):
    # вычисляем расстояние между двумя точками
    x = canvas.coords(ball1.oval)[2] - ball1.r
    y = canvas.coords(ball1.oval)[3] - ball1.r
    rasstoyanie = ((x - event.x) ** 2 + (y - event.y) ** 2) ** 0.5

    if rasstoyanie <= ball1.r:
        global score, route
        score += 1
        label_score['text'] = 'Очки: ' + str(score)
        #canvas.delete(ball1.oval)
        # route = choice(routes)
        # create_boll()


def main():
    global root, canvas, ball1, label_score

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

from random import randrange as rnd, choice
from tkinter import *
from time import sleep

routes = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
colors = ['red', 'orange', 'yellow', 'green', 'blue']
#score = 0
speed_animation = 5


class Boll:
    def __init__(self):
        self.step_animation = 1
        self.r = rnd(30, 50)
        self.x = rnd(self.r, 700)
        self.y = rnd(self.r, 500)
        self.id = canvas.create_oval(self.x - self.r, self.y - self.r,
                                     self.x + self.r, self.y + self.r,
                                     fill=choice(colors))
        self.route = choice(routes)

    def change_route(self):
        """
        меняем направление движения и цвет шарика
        """

        try:
            x1 = canvas.coords(self.id)[0]
            y1 = canvas.coords(self.id)[1]
            x2 = canvas.coords(self.id)[2]
            y2 = canvas.coords(self.id)[3]
        except Exception:
            x1 = y1 = x2 = y2 = 0
            print('ERROR')

        if x1 < 1:
            possibly_route = ['N', 'NE', 'E', 'SE', 'S']
        elif y1 < 1:
            possibly_route = ['E', 'SE', 'S', 'SW', 'W']
        elif x2 > 799:
            possibly_route = ['N', 'S', 'SW', 'W', 'NW']
        elif y2 > 599:
            possibly_route = ['N', 'NE', 'E', 'W', 'NW']

        if x1 < 1 or y1 < 1 or x2 > 799 or y2 > 599:
            self.route = choice(possibly_route)
            canvas.itemconfig(self.id, fill=choice(colors))

    def move_boll(self):
        """
        двигаем шарик в зависимости от выбранного направления
        """

        if self.route == 'E' or self.route == 'NE' or self.route == 'SE':
            x = self.step_animation
        elif self.route == 'W' or self.route == 'NW' or self.route == 'SW':
            x = -self.step_animation
        else:
            x = 0

        if self.route == 'N' or self.route == 'NE' or self.route == 'NW':
            y = -self.step_animation
        elif self.route == 'S' or self.route == 'SE' or self.route == 'SW':
            y = self.step_animation
        else:
            y = 0

        canvas.move(self.id, x, y)

    def delete_boll(self):
        canvas.delete(self.id)


class BattleField:
    def __init__(self):
        pass

    def update_battle_field_with_miss(self):
        pass


def tick():
    boll_1.change_route()
    boll_1.move_boll()

    root.after(speed_animation, tick)


def click(event):
    global score, label_score,  boll_1, canvas

    # вычисляем расстояние между двумя точками
    # первая точка это середина мячика
    # вторая точка это позиция мышки во время клика мышкой
    x = canvas.coords(boll_1.id)[2] - boll_1.r
    y = canvas.coords(boll_1.id)[3] - boll_1.r
    distance = ((x - event.x) ** 2 + (y - event.y) ** 2) ** 0.5

    boll_1.delete_boll()

    if distance <= boll_1.r:
        score += 1
    else:
        canvas.config(background="red")
        canvas.update()
        sleep(0.1)
        canvas.config(background="white")
        score = 0

    boll_1 = Boll()
    label_score['text'] = 'Очки: ' + str(score)


def main():
    global root, canvas, boll_1, label_score

    root = Tk()
    root.geometry('800x600')
    canvas = Canvas(root, bg='white')
    label_score = Label(bg='gray', fg='white', text='Очки: 0', width=800)
    canvas.pack(fill=BOTH, expand=1)
    label_score.pack()

    canvas.bind('<Button-1>', click)

    boll_1 = Boll()
    tick()
    root.mainloop()


if __name__ == '__main__':
    main()

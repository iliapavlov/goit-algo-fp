import turtle
import math

def draw_branch(t, length, angle, depth):
    if depth == 0:
        return

    t.forward(length)

    pos = t.pos()
    heading = t.heading()

    # Ліва гілка
    t.left(angle)
    draw_branch(t, length * math.cos(math.radians(angle)), angle, depth - 1)

    # Повертаємось
    t.setpos(pos)
    t.setheading(heading)

    # Права гілка
    t.right(angle)
    draw_branch(t, length * math.cos(math.radians(angle)), angle, depth - 1)

    # Повертаємось
    t.setpos(pos)
    t.setheading(heading)

def draw_fractal_tree():
    screen = turtle.Screen()
    screen.bgcolor("lightblue")
    screen.title("Фрактал \"дерево Піфагора\"")

    t = turtle.Turtle()
    t.speed(0)
    t.color("midnightblue")
    t.pensize(2)
    t.left(90)
    t.penup()
    t.goto(0, -250)
    t.pendown()

    length = 100
    angle = 45

    try:
        depth = int(input("Вкажіть рівень рекурсії (наприклад, 5): "))
        if depth < 0 or depth > 15:
            print("Будь ласка, введіть значення від 0 до 15.")
            return
    except ValueError:
        print("Некоректне значення. Введіть ціле число.")
        return

    draw_branch(t, length, angle, depth)
    screen.mainloop()
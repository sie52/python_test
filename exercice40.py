import turtle

class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def tracer_figure(self):
        t = turtle.Turtle()
        for i in range(2):
            if i == 0:
                t.pencolor("red")
            else:
                t.pencolor("blue")
            t.forward(self.longueur)
            t.left(90)
            t.forward(self.largeur)
            t.left(90)
        t.hideturtle()

        turtle.done()


if __name__ == "__main__":
    rect = Rectangle(100, 50)

    rect.tracer_figure()

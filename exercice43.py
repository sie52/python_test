import turtle

class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def draw(self):
        t = turtle.Turtle()
        t.fillcolor("black")
        t.pencolor("red")
        t.begin_fill()
        for _ in range(2):
            t.forward(self.longueur)
            t.left(90)
            t.forward(self.largeur)
            t.left(90)
        t.end_fill()

class Square(Rectangle):
    def __init__(self, côté, inclinaison=30):
        super().__init__(côté, côté)
        self.inclinaison = inclinaison

    def draw(self):
        t = turtle.Turtle()
        t.fillcolor("black")
        t.pencolor("red")
        t.begin_fill()
        t.left(self.inclinaison)  
        for _ in range(4):
            t.forward(self.longueur)
            t.left(90)
        t.end_fill()

if __name__ == "__main__":
    rect = Rectangle(100, 50)
    rect.draw()

    square = Square(100)
    square.draw()

turtle.done()

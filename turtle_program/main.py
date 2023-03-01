import turtle

def escalier(size, nbr):
  for i in range(0,nbr):
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.right(90)
  t.forward(size)


def carre(size):
  for i in range(0, 4):
    t.forward(size)
    t.left(90)


def carres(size_init, nbr):
  for i in range(0, nbr):
    carre(size_init * (i + 1))

t = turtle.Turtle()

# escalier(30,5)
# carre(100)
carres(10, 10)

turtle.done()
from turtle import*
#'transmitting' = True
print('Green is a radiowave')
hideturtle()
clear()
penup()
goto(0, 100)
pendown()
forward(50)
left(180)
forward(100)
penup()
goto(0, -100)
pendown()
forward(50)
left(180)
forward(100)

penup()
goto(0, 150)
pendown()
write('object blocking radar radio waves', font = 'arial')

penup()
goto(0, -150)
pendown()
write('radar transmitting radio waves', font = 'arial')
penup()
#register_shape('wave',(5,5), (5,-5), (0,0))
shape('circle')
goto(0, -100)
showturtle()
left(90)
pendown()
size = 0
color('green')
while True:
  forward(200)
  left(180)

while True:
   size = size + 1
   pensize(size)
   distance = 0
while (distance < 200):
    size = size + 0.1
    pensize(size)
    color(distance % 255)
    distance = distance + 1
    forward(1)
    left(180)

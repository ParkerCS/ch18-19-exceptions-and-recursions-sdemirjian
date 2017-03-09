'''
Using the turtle library, create a fractal pattern.
You may use heading/forward/backward or goto and fill commands to draw
your fractal.  Ideas for your fractal pattern might include
examples from the chapter.  You can find many fractal examples online,
but please make your fractal unique.  Experiment with the variables
to change the appearance and behavior.

Give your fractal a depth of at least 5.  Ensure the fractal is contained on the screen (at whatever size you set it).  Have fun.
(35pts)
'''
import turtle

#Before you run: You can close the turtle window at any time. I made so many recursions because without it it wouldn't form such a nice design. Enjoy!

my_turtle = turtle.Turtle()
my_screen = turtle.Screen()

color_list = ["red", "orange", "yellow", "green", "blue", "purple", "brown", "grey", "black"]

def fractal(x, y, heading, dist, depth):
    my_turtle.up()
    my_turtle.goto(x,y)
    my_turtle.color(color_list[depth%len(color_list)])
    my_turtle.down()
    my_turtle.setheading(heading)
    my_turtle.forward(dist)

    new_y = my_turtle.ycor()
    new_x = my_turtle.xcor()

    if depth > 0:
        fractal(new_x, new_y, heading + 10, dist/1.2, depth - 1)
        fractal(new_x, new_y, heading - 50, dist/1.2, depth - 1)

my_turtle.speed(0)
fractal(-250,-220,45,100,12)
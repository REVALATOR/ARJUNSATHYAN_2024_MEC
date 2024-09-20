import turtle
import math
scr=turtle.Screen()
scr.title("design")
t=turtle.Turtle()
t.width(5)
t.speed(0)

def fillcircle(radius,color):
    t.color(color)
    t.penup()
    t.setheading(270)
    t.fd(radius)
    t.setheading(0)
    t.pendown()
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    t.penup()
    t.setheading(90)
    t.fd(radius)
    t.setheading(10)
    t.pendown()


def cs(a,b,c,d,fill_color):
    org_pos=t.pos()
    org_heading=t.heading()
    t.color("orange")
    t.speed(0)
    angle=360/b
    for i in range(b):
        theta=math.radians(i*angle)
        center_x=a*math.cos(theta)
        center_y=a*math.sin(theta)
        t.penup()
        t.goto(center_x,center_y - c)
        t.pendown()
        if d==1:
            t.fillcolor(fill_color)
            t.begin_fill()
        t.circle(c)
        if d==1:
            t.end_fill()

    t.penup()
    t.goto(org_pos)
    t.setheading(org_heading)
    t.pendown()
fillcircle(170,"brown")
cs(160,12,10,1,"white")
fillcircle(140,"green")



t.speed(0)
for i in range(180):
    for j in ("orange","yellow","red"):
        t.color(j)
        t.forward(i)
        t.right(80)
t.penup()
t.goto(0,0)
t.pendown()
fillcircle(60, "white")
t.penup()
t.goto(0,0)
t.pendown()
fillcircle(40, "pink")
t.penup()
t.goto(0,0)
t.pendown()

def draw_petal(t, color):
    t.fillcolor(color)
    t.begin_fill()
    t.circle(70, 60)  # Draw the arc of the petal
    t.left(120)        # Turn to draw the other side of the petal
    t.circle(70, 60)  # Draw the arc of the petal
    t.left(120)
    t.end_fill()

def draw_flower():
    t.speed(0)        # Set the drawing speed
    for i in range(6):
        draw_petal(t, "purple")
        t.right(60)  # Rotate to position for the next petal

# Run the flower drawing function
draw_flower()
t.penup()
t.goto(0,0)
t.pendown()
fillcircle(10, "brown")
t.hideturtle()
turtle.done()




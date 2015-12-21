import turtle

def load_window():
    window = turtle.Screen()
    window.bgcolor("red")
load_window()
def draw_a_square() :
    bug = turtle.Turtle()
    bug.shape("turtle")
    val = 0
    while(val<4):
        bug.forward(100)
        bug.right(90)
        val = val +1
#draw_a_square()        
def draw_a_circle():
    circle = turtle.Turtle()
    circle.circle(100)
#draw_a_circle()
def draw_rhombus(some_turtle):
    for i in range(1,4):
        some_turtle.forward(75)
        some_turtle.right(60)
        some_turtle.forward(100)
        some_turtle.right(120)
        some_turtle.forward(100)
        some_turtle.right(60)
        some_turtle.forward(75)
#draw_flower()    

def draw_a_triangle(some_turtle) :
    for i in range(1,4):
        some_turtle.forward(150)
        some_turtle.right(120)
def sketch_a_flower (): 
    bug = turtle.Turtle()
    bug.speed(30)
    bug.shape("turtle")
    bug.color("yellow")
    for i in range(1,37):
     draw_rhombus(bug)
     bug.right(50)
    bug.right(90)
    bug.forward(300)
sketch_a_flower()
def exit_window():
    window = turtle.Screen()
    window.exitonclick()    
exit_window()

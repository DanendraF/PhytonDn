import turtle  
t = turtle.Turtle()  

s = turtle.Screen()  
s.bgcolor("blue")  
  
turtle.pensize(2)  
  
# To design curve  
def curve():  
    for i in range(200):  
        t.right(1)  
        t.forward(1)  
  
t. speed(10)  
t.color("orange", "pink")  
  
t.begin_fill()  
t.left(140)  
t.forward(111.65)  
curve()  
  
t.left(120)  
curve()  
t.forward(111.65)  
t.end_fill()  
t.hideturtle()

turtle.mainloop()  

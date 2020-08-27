import easygui
import turtle


reply=easygui.buttonbox("Select shape",choices=['circle','triangle'])
t=turtle.Pen()
turtle.setup(width=550, height=400)

if reply=='circle':
    number=easygui.enterbox("Enter number of circle to draw")
    number=int(number)
    for i in range (number):
        if i%2==1:
            t.setheading(0)
            t.circle(20)
            t.up()
            t.forward(80)
            t.down()
        else:
            t.setheading(0) 
            t.circle(20)
            t.up()
            t.forward(40)
            t.down()
            
            
elif reply=='triangle':
    number=easygui.enterbox("Enter number of triangle to draw")
    number=int(number)
    for i in range (number):
        if i%2==1:
            t.up()
            t.forward(60)
            t.down()
            for i in range(3):
                t.forward(30)
                t.left(120)
            t.up()
            t.forward(30)
            t.down()
        else:
            for i in range(3):
                t.forward(30)
                t.left(120)
    

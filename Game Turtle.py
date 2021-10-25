import keyboard 
from turtle import Turtle, Screen
import turtle

screen = Screen()
t = Turtle()
t.write(arg="باز گشت:h \t چرخش 90 درجه:A \t Sچرخش 5 درجه\t مکان دقیقg \tstap:p\tdot:d\tحرکت:space\n\n\n\n\n\n\n\n\n\n\n\n\n\n", align="center", font=("B Kamran", 10, "normal"))

t.right(270)
pc=turtle.textinput("Pen Color", "What is Pen Color")
t.pencolor(pc)
bg=turtle.textinput("Background Color", "What is Background Color")
turtle.bgcolor (bg)
t.pensize(5)
t.shapesize(1.5)
t.fillcolor('Green')
turtle.title ("Turtle Painter")
def FoR():
    t.forward(30)
    Loop()
def Back():
    t.backward(30)
    Loop()
def A_90():
    t.right(90)
    Loop()
    Loop()
def S_5R():
    t.right(5)
    Loop()
def start_c():
    turtle.begin_fill()
    t.forward(30)
    Loop()
def StopD():
    turtle.end_fill()
    t.forward(30)
    Loop()
def screenShot():
    import pyscreenshot as ImageGrab
    # fullscreen
    im=ImageGrab.grab()
    im.show()
    im=ImageGrab.grab(bbox=(10,10,500,500))
    im.show()
    ImageGrab.grab_to_file('im.png')
    Loop()
def Loop():

    while True:


        t.shape("turtle")
        if keyboard.is_pressed('p') or keyboard.is_pressed('P'):
            turtle.stamp()
        if keyboard.is_pressed('c') or keyboard.is_pressed('C'):
            t.circle (90)
        if keyboard.is_pressed('g') or keyboard.is_pressed('G'):
            x=turtle.textinput("X", "Enter x")
            y=turtle.textinput("Y", "Enter y")
            turtle.goto (int(x),int(y))
        if keyboard.is_pressed('ctrl+space')  :
            start_c()
            turtle.mainloop()
            break
        if keyboard.is_modifier('ctrl+space'):
            StopD()
            turtle.mainloop()
            break
        if keyboard.is_pressed('h') or keyboard.is_pressed('H'):
            t.home()
            t.left(90)
        if keyboard.is_pressed('d') or keyboard.is_pressed('D'):
            t.dot(20)
        if keyboard.is_pressed(' ') or keyboard.is_pressed(' '):
            FoR()
            turtle.mainloop()
            break
        if keyboard.is_pressed(' ') and keyboard.is_pressed('Shift'):
            print("For")
            turtle.mainloop()
            break
        if keyboard.is_pressed('b') or keyboard.is_pressed('B'):
            Back()
            turtle.mainloop()
            break
        if keyboard.is_pressed('a') or keyboard.is_pressed('A'):
            A_90()
            turtle.mainloop()
            break
        if keyboard.is_pressed('s') or keyboard.is_pressed('S'):
            S_5R()
            turtle.mainloop()
            break
        if keyboard.is_pressed('i')or keyboard.is_pressed('I'):
            screenShot()
            turtle.mainloop()
            break
Loop()

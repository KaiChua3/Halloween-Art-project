# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
fill_color = "blue"
shape_size = 3
shape = "triangle"

#-----initialize turtle-----
painter = trtl.Turtle()
painter.shape("triangle")
painter.shapesize(3)
painter.fillcolor("blue")

#-----game functions--------
def painter_clicked(x,y):
    change_position()
def change_position():
    new_xpos = rand.randint(-400,400)
    new_ypos = rand.randint(-300,300)
    painter.penup() 
    painter.goto(new_xpos,new_ypos)
def halloween_picture():
    picture = rand.choice(0,2)
#-----events----------------
wn = trtl.Screen()
wn.addshape('halloween-2019-blog-1-1.gif')
wn.addshape('download.gif')
wn.addshape('halloween-gettyimages-172988453.gif')
painter.onclick(painter_clicked)
wn.mainloop()
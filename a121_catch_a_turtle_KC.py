# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
fill_color = "blue"
shape_size = 3
shape = "triangle"
list = ["Halloween is on October 31st","Candy corn used to be called Chicken feed","Only 65% of Americans celebrate halloween","Jack'o lanterns in Ireland and Scotland was made out of turnips, beets, and potatoes instead of pumpkins",""]
#'halloween-2019-blog-1-1.gif', 'download.gif', 'halloween-gettyimages-172988453.gif'
#-----initialize turtle-----
painter = trtl.Turtle()
painter.shape("triangle")
painter.shapesize(3)
painter.fillcolor("blue")

#-----game functions--------
def painter_clicked(x,y):
    change_position()
    halloween_picture(x)
def change_position():
    new_xpos = rand.randint(-400,400)
    new_ypos = rand.randint(-300,300)
    painter.penup()
    painter.goto(new_xpos,new_ypos)
def halloween_picture(x):
    x = rand.randint(0,3)
    print(list[x])
#-----events----------------
wn = trtl.Screen()
wn.addshape('ezgif.gif')
wn.bgpic('ezgif.gif')
painter.onclick(painter_clicked)
wn.mainloop()

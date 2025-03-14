# import various libraries
import turtle
import time
import math

# make the game screen
screen=turtle.getscreen()
screenTk = screen.getcanvas().winfo_toplevel()
screenTk.attributes("-fullscreen", 1)

# hiding original turtle
turtle.ht()
turtle.Screen().bgcolor("#bdfff9")

# something to do with the screen dimensions
canvas = screen.cv
window_x = canvas.winfo_screenwidth()
window_y = canvas.winfo_screenheight()

# making the player turtle
t=turtle.Turtle()
t.ht()
t.up()
t.shape("circle")
t.color("#18ff00")

#making the enemy turtle
rec=turtle.Turtle()
rec.ht()
rec.up()
rec.shape("square")
rec.turtlesize(2,4)
rec.color("#ff1111")
rec.goto(100,60)

# making the bullet turtle
bullet=turtle.Turtle()
bullet.ht()
bullet.up()
bullet.shape("circle")

# making the turtle that draws the title and play button
title=turtle.Turtle()
t.turtlesize(3, 3, 1)
title.ht()
title.up()
play=turtle.Turtle()
play.ht()
play.pensize(width=3)
play.up()

# initialising variables
x=0 # x cor of cursor
y=0 # y cor of cursor 
direction=0 # direction of player
key_held_w = False # boolean for detecting w key being held
key_held_s = False # boolean for detecting d key being held

# list of bullets
bullets=[]

# stops time
screen.tracer(0)

# draws the title
title.clear()
title.goto(-550,250)
title.write("Rectangle Shooter", font=("Arial",60))
title.goto(0,160)
title.write("By AtrashK and 0wqlff", font=("Arial",30))

# draws the play button
play.goto(-200, -100)
play.down()
play.goto(-200,50)
play.goto(200,50)
play.goto(200,-100)
play.goto(-200, -100)
play.up()
play.goto(-65,-60)
play.write("Play", font=("Arial", 50))

Screen="home" # sets the screen to homescreen

# unfreezes time
screen.update()

# what happens when the cursor is clicked
def click(x,y): 
    global Screen, t, bullet, bullet1, window_x, window_y, bullets, newbullet
    if (Screen=="home"): # if the play button is clicked
        if (x<=200 and x>=-200 and y<=50 and y>=-100): # if the play button is clicked # and is on homescreen, then starts game function
            Screen="game"
            t.st() 
            rec.st()
            game()
                   
    elif (Screen=="game"): # for shooting
        newbullet = bullet.clone()
        newbullet.st()
        newbullet.goto(bullet.xcor(),bullet.ycor())
        bullets.append(newbullet)

def update_bullet():
    for bullet in bullets[:]:
        bullet.fd(15)        
        if (bullet.xcor()>window_x or bullet.xcor()<-window_x or bullet.ycor()>window_y or bullet.ycor()<-window_y):
            bullet.hideturtle()
            bullets.remove(bullet)

def check_collisions():
    global newbullet, t, rec
    if (newbullet.xcor()>100):
        rec.ht()


    


def press_w():
    global key_held_w
    key_held_w = True

def release_w():
    global key_held_w
    key_held_w = False

def press_s():
    global key_held_s
    key_held_s = True

def release_s():
    global key_held_s
    key_held_s = False

def movement():
    global key_held_w, key_held_s
    if key_held_w:
        t.forward(7)
    if key_held_s:
        t.forward(-7)

def dir():
    global direction, x, y, t, rec, tdir
    direction = math.degrees(math.atan((y-t.ycor())/(x-t.xcor()+1e-9))) 
    if (x<t.xcor() and y>t.ycor()):
        direction = 180+direction
    if (x<t.xcor() and y<t.ycor()):
        direction = -180+direction
    t.seth(direction)
    tdir=math.degrees( math.atan( ( ( t.ycor()-rec.ycor() )/( t.xcor()-rec.xcor() ) ) ) )
    rec.seth(tdir+180)


def track_cursor():
    global x, y, window_x, window_y
    x, y = screen.cv.winfo_pointerx(), screen.cv.winfo_pointery()
    canvas = screen.cv

    window_x = canvas.winfo_screenwidth()
    window_y = canvas.winfo_screenheight()

    x=x-798.5
    y=-(y-445)


def game():
    global Screen, play, title, x, y, direction, t, bullet, rec
    play.clear()
    title.clear()

    Screen="game"

    track_cursor()
    dir()

    screen.listen()
    screen.onkeypress(press_w, "w")  
    screen.onkeyrelease(release_w, "w")
    screen.onkeypress(press_s, "s")  
    screen.onkeyrelease(release_s, "s")
    screen.onclick(click)

    screen.tracer(0)
    movement()

    track_cursor()
    check_collisions()
    dir()

    bullet.setheading(t.heading())
    bullet.setx(t.xcor())
    bullet.sety(t.ycor())

    #print(rec.seth())

    update_bullet()

    screen.update()
    screen.ontimer(game, 20)
    
screen.listen()
screen.onclick(click)

screen.mainloop()
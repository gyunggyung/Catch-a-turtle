import turtle as t
import random

score = 0
playing = False
counter = 0
shadow = False
booster = 1

def create_turtle(name, color,x,y,role):
	global test
	if role == 0:
		name.shape("turtle")
	else:
		name.shape("circle")
	name.color(color)
	name.speed(0)
	name.up()
	name.goto(x,y)

ta = t.Turtle()
create_turtle(ta,"red",-100,200,0)

ta2 = t.Turtle()
create_turtle(ta2,"red",100,200,0)

ts = t.Turtle()
create_turtle(ts,"green",0,-200,1)

sh = t.Turtle()
create_turtle(sh,"blue",100,-200,1)

def turn_right():
	t.setheading(0)

def turn_up():
	t.setheading(90)

def turn_left():
	t.setheading(180)

def turn_down():
	t.setheading(270)

def boost():
	global booster
	if booster > 0:
		t.forward(100)
		booster = booster - 1

def start():
	global playing
	if playing == False:
		playing = True
		t.clear()
		play()

def atta(atk):
	global score
	global counter
	global shadow
	global booster
	if random.randint(1, 5) == 2:
		ang = atk.towards(t.pos())
		atk.setheading(ang)
	speed = score + 5
	if speed > 15:
		speed = 15
	atk.forward(speed)

	if t.distance(ts) < 12:
		score = score + 1
		t.write(score)
		star_x = random.randint(-230, 230)
		star_y = random.randint(-230, 230)
		ts.goto(star_x, star_y)
		shadow = False
		booster=booster + 1

	if t.distance(sh) <12:
		score = score + 1
		star_x = random.randint(-230, 230)
		star_y = random.randint(-230, 230)
		sh.goto(star_x, star_y)
		shadow = True
		booster= booster + 1

def play():
	global playing
	global score
	global shadow
	global booster
	t.forward(10)
	atta(ta)
	atta(ta2)
	if shadow :
		t.bgcolor("red")
	else:
		t.bgcolor("purple")
	if t.distance(ta) <= 12 or t.distance(ta2) <= 12:
		text = "Score : "+str(score)
		message("You are caught.", text, "if you want to do it again, pressthe space key")
		playing = False
		score = 0
		booster = 0
		t.onkeypress(start, "space")
	if playing :
		t.ontimer(play, 100)

def message(m1, m2, m3):
	t.clear()
	t.goto(0, 100)
	t.write(m1, False, "center", ("", 20))
	t.goto(0, -100)
	t.write(m2, False, "center", ("", 15))
	t.goto(0, -150)
	t.write(m3, False, "center", ("", 10))
	t.home()
t.setup(500, 500)
t.bgcolor("purple")
t.shape("turtle")
t.speed(0)
t.up()
t.color("white")
t.onkeypress(turn_right,"Right")
t.onkeypress(turn_up, 	"Up")
t.onkeypress(turn_left,	"Left")
t.onkeypress(turn_down,	"Down")
t.onkeypress(start, "space")
t.onkeypress(boost, "b")
t.listen()
t.mainloop()

from turtle import*
#we want to paint a house

#step 1: draw a square

penup()
goto(-100, -70)
pendown()

speed(50)
width(7)
color("purple") 
forward(100)
left(90)

forward(200)
left(90) 

forward(200)
left(90)

forward(200)
left(90)
forward(50) 
left(90)

#end of square

#step 2: make a door for the house

color("red") 
begin_fill()
forward(90)
right(80)

forward(40)
right(90)

forward(95)
end_fill()

penup()
goto(100, 120)
pendown()

color("red")
begin_fill()

right(90)
forward(200)

left(120)
forward(200)









exitonclick()
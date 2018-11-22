from turtle import forward,left,right,exitonclick,color
from random import choice

colors = ["gold", "red", "blue", "pink", "green","purple","black"]

for x in range(1000000):
	color(choice(colors))
	forward(x / 100)
	left(9)

exitonclick()
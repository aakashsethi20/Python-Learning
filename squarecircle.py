#!/usr/bin/python

import turtle

def draw_square(some_turtle) :
	for i in range(0, 4):
		some_turtle.forward(100)
		some_turtle.right(90)

def draw_art() :
	window = turtle.Screen()
	window.bgcolor("red")

	# Turtle brad will draw the art
	brad = turtle.Turtle()
	brad.shape("classic")
	brad.color("yellow")
	for i in range(0, 36) :
		draw_square(brad)
		brad.right(10)

	window.exitonclick()

draw_art()
from tkinter import N
import turtle
import colorsys

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.speed(0)
n = 36
h = 0
for i in range(360):
    c = colorsys.hsv_torgb(h, 1, 0.8)
    h+= 1/n
    t.color(c)
    t.circle(180)
    t.left(10)
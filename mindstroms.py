__author__ =  "Gangadhar Mylapuram"

#import turtle
from turtle import Turtle
from turtle import Screen

def draw_triangle(bot, angle):
    bot.rt(angle)
    sides = 3
    while (sides != 0) :
        bot.left(120);
        bot.fd(150);
        sides =  sides - 1
   

def draw_square(bot, angle):
    #bot = turtle.Turtle();
    bot.rt(angle)
    #bot.setpos(x,y)
    #bot.st()
    sides = 4
    while (sides != 0) :
        bot.left(90);
        bot.fd(150);
        sides =  sides - 1
    #bot.clear()

def draw_circle(bot, x, y):
    #bot = turtle.Turtle();
    #bot.ht()
    bot.shape("circle");
    bot.color("green");
    bot.speed("slowest");
    #bot.setpos(x, y)
    #bot.st()
    bot.circle(50);
    bot.clear()
    
window = Screen();
window.bgcolor("yellow");

#draw_triangle(3, 100, 100)
#draw_square(4, 200, 200)
#draw_circle(300, 300)

# 1. don't show trutle shape.
# 2. we need to draw multiple squres (360/10 = 36 squares)
# 3. each squre we should start with different angle (10 degrees).
# 4. for each square, createa turtle and call square function.

bot = Turtle()
#bot.ht()
bot.color("blue", "green");
bot.speed("fast");
bot.begin_fill()
for i in range(0, 36):
    print (" square " + str(i * 10))
    draw_triangle(bot, 10)
bot.end_fill()

window.exitonclick()

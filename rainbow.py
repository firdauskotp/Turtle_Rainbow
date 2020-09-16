from turtle import *

tom = Turtle()
tom.shape('turtle')
tom.color('green')
tom.speed(0)
def rainbow(c,l,r,l2):
    tom.color(c)
    tom.begin_fill()
    tom.forward(l)
    tom.left(90)
    tom.circle(-r,180)
    tom.setheading(0)
    tom.forward(l)
    tom.left(90)
    tom.circle(l2,180)
    tom.setheading(0)
    tom.end_fill()
    tom.forward(100/7)
    
test_l=100 #forward
test_r=100 #Small semi circle
test_l2=200 #Big semi circle
test_div=100/7 #To divide among 7 colours/segments
box=['red','orange','yellow','green','blue','indigo','violet'] #le colours
for x in range(7):
    rainbow(box[x],test_l,test_r,test_l2)
    test_l=test_l-test_div
    test_l2=test_l2-test_div

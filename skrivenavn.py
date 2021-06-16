from turtle import*


def S():
    
    
    for i in range(3):
        backward(100)
        right(90)
        
    penup()
    backward(100)
    right(90)
    
    pendown()


    
    for i in range(2):
        right(90)
        forward(100)
        
def I():
    forward(200)
    
S()
penup()
backward(200)
right(90)
pendown()
I()


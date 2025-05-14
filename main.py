import turtle as t

class Chess_pieces (t.Turtle):
    def __init__(self,x,y):
        t.Turtle.__init__(self)
        self.speed(0)
        self.up()
        positions[f"{x},{y}"] = self
        self.goto(return_center_square(x,y))
        
        
class King (Chess_pieces) :
    def __init__(self, x, y, color):
        Chess_pieces.__init__(self,x,y)
        if color == "w" :
            self.shape(r"2.0/image/White_KING.gif")
        elif color == "b" :
            self.shape(r"2.0\image\Black_KING.gif")
        

def return_cordinate (x,y) :
    return(x//90+5,y//90+5)
    
def return_center_square (x,y) :
    x = x*90+45-450
    y = y*90+45-450
    return (x,y)

turn = "w1"



screen = t.Screen()

screen.bgpic(r'2.0\image\board_rotate.gif')
screen.setup(720,720)

screen.register_shape(r"2.0/image/White_KING.gif")
screen.register_shape(r"2.0\image\Black_KING.gif")



positions = {}

yellow_square = t.Turtle()
yellow_square.up()
yellow_square.color('yellow')
yellow_square.shape("square")
yellow_square.shapesize(4.5)
yellow_square.speed(0)
yellow_square.hideturtle()
canvas = screen.getcanvas()
for tag in canvas.find_withtag(str(yellow_square)):
    canvas.tag_lower(tag)

def yellow_square_follow_pointer (x,y) :
    yellow_square.showturtle()
    x,y = return_cordinate(x,y)
    x,y = return_center_square(x,y)
    yellow_square.goto(x,y)
    
King(5,1,"w")
King(5,8,"b")

print(positions)
    
screen.onclick(yellow_square_follow_pointer)

screen.mainloop()
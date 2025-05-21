import turtle as t

class Chess_pieces (t.Turtle):
    def __init__(self,x,y,color):
        t.Turtle.__init__(self)
        self.speed(0)
        self.up()
        positions[f"{x},{y}"] = {"object":self,"color":color}
        self.goto(return_center_square(x,y))
        
        
class King (Chess_pieces) :
    def __init__(self, x, y, color):
        Chess_pieces.__init__(self,x,y,color)
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

turn = {"target_color":"w","target_action":"check_what_to_move"}

piece_in_action = None


screen = t.Screen()

screen.bgpic(r'2.0\image\board_rotate.gif')
screen.setup(720,720)

screen.register_shape(r"2.0/image/White_KING.gif")
screen.register_shape(r"2.0\image\Black_KING.gif")


screen.register_shape(r"C:\Users\Lenovo\Downloads\Webp.net-resizeimage.gif")



positions = {}

yellow_square = t.Turtle()
yellow_square.up()
yellow_square.color('yellow')
yellow_square.shape(r"C:\Users\Lenovo\Downloads\Webp.net-resizeimage.gif")
yellow_square.shapesize(4.5)
yellow_square.speed(0)
yellow_square.hideturtle()
canvas = screen.getcanvas()
for tag in canvas.find_withtag(str(yellow_square)):
    canvas.tag_lower(tag)

def yellow_square_follow_pointer (x,y) :
    yellow_square.showturtle()
    x,y = return_cordinate(x,y)
    x1,y1 = return_center_square(x,y)
    yellow_square.goto(x1,y1)
    
    for i in positions.keys() :    # check if touch a chess piece
        check = f"{int(x)},{int(y)}"
        # print(check,i)
        # positions[i] --> {target_object,color}
        if check == i :
            if positions[i]['color'] == turn["target_color"] :
                piece_in_action = positions[i]['object']

                

    
King(5,1,"w")
King(5,8,"b")

    
screen.onclick(yellow_square_follow_pointer)

screen.mainloop()
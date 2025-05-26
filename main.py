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
    def check_move (self,xfrom,yfrom,xto,yto) :
        # print(f"{xfrom},{yfrom} to {xto},{yto}")
        
        if abs(xfrom-xto) <=1 and abs(yfrom-yto) <= 1 :
            if f"{xto},{yto}" in positions :
                positions[f"{xto},{yto}"]['object'].hideturtle()
            
            self.goto(return_center_square(xto,yto))
            del positions[f"{xfrom},{yfrom}"]
            positions[f"{xto},{yto}"] = {"object":self,"color":turn['target_color']}
            return True
        else :
            return False
        
class Rook (Chess_pieces) :
    def __init__(self, x, y, color):
        Chess_pieces.__init__(self,x,y,color)
        if color == "w" :
            self.shape(r"2.0\image\White_rook.gif")
        elif color == "b" :
            self.shape(r"2.0\image\Black_rook.gif")
    def check_move (self,xfrom,yfrom,xto,yto) :
        # print(f"{xfrom},{yfrom} to {xto},{yto}")
        # print('check move for rook activated')
        # print('x',xfrom == xto,', y',yfrom == yto)
        if (xfrom == xto) ^ (yfrom == yto) :
            if xfrom == xto : #change in y
                # print('form',xfrom,yfrom,'to',xto,yto,'change Y')
                range_to_check = yto-yfrom
                step = (range_to_check > 0) - (range_to_check < 0) # 1/-1
                for i in range(yfrom+step,range_to_check+yfrom+step,step) : 
                    # print(f"{xfrom},{i}")
                    if f"{xfrom},{i}" in positions :   #if find other color piece between, change x,y to and stop     have to check color
                        if (positions[f"{xfrom},{i}"]['color'] != turn["target_color"]) :
                            positions[f"{xfrom},{i}"]['object'].hideturtle()
                            yto = i
                            # print('bumb')
                            break
                        else :
                            return False
            elif yfrom == yto :#change in x
                # print('form',xfrom,yfrom,'to',xto,yto,'change X')
                range_to_check = xto-xfrom
                step = (range_to_check > 0) - (range_to_check < 0)
                for i in range(step+xfrom,xfrom+step+range_to_check,step) :
                    # print(f"{i},{yfrom}")
                    if f"{i},{yfrom}" in positions :   #if find other color piece between, change x,y to and stop
                        if positions[f"{i},{yfrom}"]['color'] != turn['target_color'] :
                            positions[f"{i},{yfrom}"]['object'].hideturtle()
                            xto = i
                            # print('bumb')
                            break
                        else :
                            return False
            
            
            self.goto(return_center_square(xto,yto))
            del positions[f"{xfrom},{yfrom}"]
            positions[f"{xto},{yto}"] = {"object":self,"color":turn['target_color']}
            return True
        else :
            return False

        

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

for i in [r"2.0/image/White_KING.gif",r"2.0\image\Black_KING.gif",
          r"2.0\image\White_rook.gif",r"2.0\image\Black_rook.gif",
          r'2.0\image\Black_knight.gif',r'2.0\image\White_knight.gif',
          r'2.0\image\Black_bishop.gif',r'2.0\image\White_bishop.gif',
          r'2.0\image\Black_Queen.gif',r'2.0\image\White_Queen.gif',
          r'2.0\image\Black_Pawn.gif',r'2.0\image\White_Pawn.gif',
          r'2.0\image\yellowsquare_resize.gif'] :
    screen.register_shape(i)



positions = {}

yellow_square = t.Turtle()
yellow_square.up()
yellow_square.color('yellow')
yellow_square.shape(r"2.0\image\yellowsquare_resize.gif")
yellow_square.shapesize(4.5)
yellow_square.speed(0)
yellow_square.hideturtle()
canvas = screen.getcanvas()
for tag in canvas.find_withtag(str(yellow_square)):
    canvas.tag_lower(tag)

def yellow_square_follow_pointer (x,y) :
    global turn,piece_in_action
    
    yellow_square.showturtle()
    x,y = return_cordinate(x,y)
    x,y = int(x),int(y)
    x1,y1 = return_center_square(x,y)
    yellow_square.goto(x1,y1)
    
    
    if turn["target_action"] == "check_what_to_move" :
        check = f"{x},{y}"  # "x,y"
        for i in positions :    # check if touch a chess piece
            if check == i :
                if positions[i]['color'] == turn["target_color"] :# positions[i] --> {target_object,color}
                    piece_in_action = {"piece":positions[i]['object'],'position':(x,y)}
                    turn["target_action"] = "check_where_to_move"
                    # print(piece_in_action)
    elif turn['target_action'] == "check_where_to_move" :
        
        if f"{x},{y}" in positions and (positions[f"{x},{y}"]['color'] == turn["target_color"]): #left to right    so it wont error
            piece_in_action = {"piece":positions[f"{x},{y}"]['object'],'position':(x,y)}
        else :        
            xfrom,yfrom = piece_in_action['position']
            condition = piece_in_action["piece"].check_move(xfrom,yfrom,x,y)
            
            if condition :
                turn["target_action"] = 'check_what_to_move'
                # print(piece_in_action,'goto',x,y)
                if turn['target_color'] == "w" :
                    turn['target_color'] = 'b'
                elif turn["target_color"] == 'b' :
                    turn["target_color"] = 'w'

                

    
King(5,1,"w")
King(5,8,"b")
Rook(1,1,'w')
Rook(8,1,'w')
Rook(1,8,'b')
Rook(8,8,'b')

    
screen.onclick(yellow_square_follow_pointer)

screen.mainloop()
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
        if (xfrom == xto) ^ (yfrom == yto) : # a xor b
            x_tochange = (xto-xfrom > 0) - (xto-xfrom < 0)
            y_tochange = (yto-yfrom > 0) - (yto-yfrom < 0)
            xtogo = xfrom
            ytogo = yfrom
            # print('x :',xtogo,'y :',ytogo)
            # print('x :',(xtogo != xto),'y :',(ytogo != yto))
            while (xtogo != xto) or (ytogo != yto) :
                xtogo += x_tochange
                ytogo += y_tochange
                # print('x :',xtogo,'y :',ytogo)
                if f'{xtogo},{ytogo}' in positions :
                    # print('something on the way')
                    if (positions[f"{xtogo},{ytogo}"]['color'] != turn["target_color"]) :
                        positions[f"{xtogo},{ytogo}"]['object'].hideturtle()
                        xto = xtogo
                        yto = ytogo
                        # print('bumb')
                        break #not nessesary
                    else :
                        return False
                
            self.goto(return_center_square(xto,yto))
            del positions[f"{xfrom},{yfrom}"]
            positions[f"{xto},{yto}"] = {"object":self,"color":turn['target_color']}
            return True
        else :
            return False
            
            
            
        
class Bishop (Chess_pieces) :
    def __init__(self, x, y, color):
        Chess_pieces.__init__(self,x,y,color)
        if color == "w" :
            self.shape(r"2.0\image\White_bishop.gif")
        elif color == "b" :
            self.shape(r"2.0\image\Black_bishop.gif")
    def check_move (self,xfrom,yfrom,xto,yto) :
        # print(f"{xfrom},{yfrom} to {xto},{yto}")
        # print('check move for bishop activated')
        # print('not devied by 0 :',xto != xfrom,', m :',(yto-yfrom)/(xto-xfrom) in [-1,1])
        
        if (xto != xfrom) and ((yto-yfrom)/(xto-xfrom) in [-1,1]) :
            # print('check move for bishop pass')
            x_tochange = (xto - xfrom > 0) - (xto - xfrom < 0)
            y_tochange = (yto - yfrom > 0) - (yto - yfrom < 0)
            
            x_togo = xfrom
            y_togo = yfrom
            while x_togo != xto and y_togo != yto :
                x_togo += x_tochange
                y_togo += y_tochange
                
                if f'{x_togo},{y_togo}' in positions :
                    if (positions[f'{x_togo},{y_togo}']['color'] != turn["target_color"]) :
                            positions[f'{x_togo},{y_togo}']['object'].hideturtle()
                            xto,yto = x_togo,y_togo
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
        

class Knight (Chess_pieces) :
    def __init__(self, x, y, color):
        Chess_pieces.__init__(self,x,y,color)
        if color == "w" :
            self.shape(r"2.0\image\White_knight.gif")
        elif color == "b" :
            self.shape(r"2.0\image\Black_knight.gif")
    def check_move (self,xfrom,yfrom,xto,yto) :
        # print(f"{xfrom},{yfrom} to {xto},{yto}")
        # print('check move for bishop activated')
        # print(type(sorted({abs(yto-yfrom),abs(xto-xfrom)})))
        
        if sorted({abs(yto-yfrom),abs(xto-xfrom)}) == [1,2] :
            # print('check move for bishop pass')
            
            if f'{xto},{yto}' in positions :
                if (positions[f'{xto},{yto}']['color'] != turn["target_color"]) :
                        positions[f'{xto},{yto}']['object'].hideturtle()
                else :
                    return False
                    
            self.goto(return_center_square(xto,yto))
            del positions[f"{xfrom},{yfrom}"]
            positions[f"{xto},{yto}"] = {"object":self,"color":turn['target_color']}
            return True
        else :
            return False


class Queen (Chess_pieces) :
    def __init__(self, x, y, color):
        Chess_pieces.__init__(self,x,y,color)
        if color == "w" :
            self.shape(r"2.0\image\White_Queen.gif")
        elif color == "b" :
            self.shape(r"2.0\image\Black_Queen.gif")
    def check_move (self,xfrom,yfrom,xto,yto) :
        # print(f"{xfrom},{yfrom} to {xto},{yto}")
        # print('check move for bishop activated')
        # print('not devied by 0 :',xto != xfrom,', m :',(yto-yfrom)/(xto-xfrom) in [-1,1])
        
        if (xto == xfrom) or ((yto-yfrom)/(xto-xfrom) in [-1,1,0]) :
            # print('check move for bishop pass')
            x_tochange = (xto - xfrom > 0) - (xto - xfrom < 0)
            y_tochange = (yto - yfrom > 0) - (yto - yfrom < 0)
            
            x_togo = xfrom
            y_togo = yfrom
            
            # print(x_togo != xto,y_togo != yto)
            while x_togo != xto or y_togo != yto :
                x_togo += x_tochange
                y_togo += y_tochange
                
                # print(x_togo,y_togo)
                if f'{x_togo},{y_togo}' in positions :
                    print('queen found something on the way')
                    if (positions[f'{x_togo},{y_togo}']['color'] != turn["target_color"]) :
                            positions[f'{x_togo},{y_togo}']['object'].hideturtle()
                            xto,yto = x_togo,y_togo
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
Bishop(3,1,'w')
Bishop(6,1,'w')
Bishop(3,8,'b')
Bishop(6,8,'b')
Knight(2,1,'w')
Knight(7,1,'w')
Knight(2,8,'b')
Knight(7,8,'b')
Queen(4,1,'w')
Queen(4,8,'b')

    
screen.onclick(yellow_square_follow_pointer)

screen.mainloop()
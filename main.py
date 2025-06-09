import turtle as t
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

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
    def __str__ (self) :
        return 'k'
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
    def __str__ (self) :
        return 'r'
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
    def __str__ (self) :
        return 'b'        
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
    def __str__ (self) :
        return 'n'
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
    def __str__ (self) :
        return 'q'
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
        
        
class Pawn (Chess_pieces) :
    def __init__(self, x, y, color):
        Chess_pieces.__init__(self,x,y,color)
        if color == "w" :
            self.shape(r"2.0\image\White_Pawn.gif")
            self.direction = 1
        elif color == "b" :
            self.shape(r"2.0\image\Black_Pawn.gif")
            self.direction = -1
        self.initial_move = True
    def __str__ (self) :
        return 'p'
    def check_move (self,xfrom,yfrom,xto,yto) :
        # print(f"{xfrom},{yfrom} to {xto},{yto}")
        
        # print(abs(yto-yfrom)<=1,(self.direction*2)>=yto-yfrom)
        if (abs(xfrom-xto) <= 1) and ((yto-yfrom)*self.direction <= 2) :#
            # print('first pawn range in condition')
            if xfrom-xto == 0 :#
                # print('pawn moving straght')
                if f'{xfrom},{yfrom + self.direction}' in positions or f"{xto},{yto}" in positions :#
                    # print('pawn have something on the way')
                    return False
                else :#
                    # print('pawn doesnt have anything on the way')
                    #print((yto-yfrom == self.direction*2),(yfrom!=int(4.5-(self.direction*2.5))))
                    if yto - yfrom == self.direction*2 and (yfrom!=int(4.5-(self.direction*2.5))) :#cd
                        #print('false na')
                        return False
                        
            
            elif (xfrom-xto != 0) and (yto-yfrom == self.direction):
                print('pawn isnt moving straght')
                if f"{xto},{yto}" in positions :
                    positions[f"{xto},{yto}"]['object'].hideturtle()
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
screen.setup(820,720)

for i in [r"2.0/image/White_KING.gif",r"2.0\image\Black_KING.gif",
          r"2.0\image\White_rook.gif",r"2.0\image\Black_rook.gif",
          r'2.0\image\Black_knight.gif',r'2.0\image\White_knight.gif',
          r'2.0\image\Black_bishop.gif',r'2.0\image\White_bishop.gif',
          r'2.0\image\Black_Queen.gif',r'2.0\image\White_Queen.gif',
          r'2.0\image\Black_Pawn.gif',r'2.0\image\White_Pawn.gif',
          r'2.0\image\yellowsquare_resize.gif'] :
    screen.register_shape(i)

button = t.Turtle()
button.shape('square')
button.speed(0)
button.up()
button.goto(385,315)
button.color('green')


positions = {}

yellow_square = t.Turtle()
yellow_square.up()
yellow_square.color('yellow')
yellow_square.shape(r"2.0\image\yellowsquare_resize.gif")
yellow_square.shapesize(4.5)
yellow_square.speed(0)
# yellow_square.hideturtle()
canvas = screen.getcanvas()
for tag in canvas.find_withtag(str(yellow_square)):
    canvas.tag_lower(tag)

def yellow_square_follow_pointer (x,y) :
    global turn,piece_in_action
    
    

    
    if abs(x) <= 360 and abs(y) <= abs(360) :
        # yellow_square.showturtle()
        x,y = return_cordinate(x,y)
        x,y = int(x),int(y)
        x1,y1 = return_center_square(x,y)
        yellow_square.goto(x1,y1)
        
        # print(positions[f'{x},{y}'])
        
        
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
    elif x > 360 and x < 410 and y < 360 and y > 270 :
        scraping()

                
charector_to_number_dict = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}

    
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

for i in range(8) :
    Pawn(i+1,2,'w')
    Pawn(i+1,7,'b')
    
def scraping () :
    button.color('red')
    
    position_dict = positions
    
    url = "https://nextchessmove.com//?fen="
    for j in range(8,0,-1) :
        n = 0
        for i in range(1,9) :
            if f'{i},{j}' in position_dict :
                if n != 0 :
                    url += str(n)
                track = position_dict[f'{i},{j}']
                if track['color'] == 'w' :
                    url += track['object'].__str__()[0].upper()
                else :
                    url +=  track['object'].__str__()[0]
                # fen += 'y'
                n = 0
            else :
                n += 1
        if n != 0 :
            url += str(n)
        url += '/'
    url = url[:-1]
    url += "%20"+turn['target_color']+r'%20-%20-%200%202'
    # print(fen)
    
    service = Service(executable_path='2.0/chromedriver.exe')
    option = Options()
    option.add_argument('--headless')
    option.add_argument('--log-level=3') # 0 = all, 1 = info, 2 = warning, 3 = error 
    option.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=service,options=option)
    
    driver.get(url)
    
    setting_button = driver.find_elements(By.XPATH, '//*[@id="ncm-main"]/div/div[1]/div[1]/div[2]/div[3]/div/div[2]/div[2]/button')
    setting_button[0].click()
    
    format_checkbox = driver.find_elements(By.XPATH,'/html/body/div[9]/div/div/div[2]/div[3]/label/input')
    format_checkbox[0].click()
    
    close_setting_button = driver.find_element(By.XPATH,'//button[@class="p-2 -mx-2"]')
    close_setting_button.click()
    
    calculate_button = driver.find_element(By.XPATH,"//button[text()='Calculate Next Move']")
    calculate_button.click()
    
    time.sleep(7)
    
    the_move = driver.find_elements(By.XPATH,"//button[@class='link']")[0].text
    
    driver.quit()
    
    print(the_move)
    # print('x =',charector_to_number_dict[the_move[0]],' y =',the_move[1])
    
    
    button.color('green')
    

    
screen.onclick(yellow_square_follow_pointer)

screen.mainloop()
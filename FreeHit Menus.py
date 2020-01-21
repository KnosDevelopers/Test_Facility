#importing necessary libraries
import pygame
import time
import os

#intializing pygame
pygame.init()

#making text input class
validChars = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"
shiftChars = '~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?'
class TextBox(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.text = ""
    self.font = pygame.font.SysFont('arial', 25)
    self.image = self.font.render("Enter your name", False, [0, 0, 0])
    self.rect = self.image.get_rect()

  def add_chr(self, char):
    global shiftDown
    if char in validChars and not shiftDown:
        self.text += char
    elif char in validChars and shiftDown:
        self.text += shiftChars[validChars.index(char)]
    self.update()

  def update(self):
    old_rect_pos = self.rect.center
    self.image = self.font.render(self.text, False, [0, 0, 0])
    self.rect = self.image.get_rect()
    self.rect.center = old_rect_pos



textBox = TextBox()
shiftDown = False
#textBox.rect.center = [320, 240]

#display dimensions
display_width = 800
display_height = 500

#display surface
gameDisplay = pygame.display.set_mode((display_width,display_height))

#function for text input class
def user_input():
    #gameDisplay = pygame.display.set_mode((display_width,display_height))
    running = True
    while running:
        gameDisplay.fill(white)
        gameDisplay.blit(textBox.image, [475,180,125,25])
        pygame.display.update()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            if e.type == pygame.KEYUP:
                if e.key in [pygame.K_RSHIFT, pygame.K_LSHIFT]:
                    shiftDown = False
            if e.type == pygame.KEYDOWN:
                textBox.add_chr(pygame.key.name(e.key))
                if e.key == pygame.K_SPACE:
                    textBox.text += " "
                    textBox.update()
                if e.key in [pygame.K_RSHIFT, pygame.K_LSHIFT]:
                    shiftDown = True
                if e.key == pygame.K_BACKSPACE:
                    textBox.text = textBox.text[:-1]
                    textBox.update()
                if e.key == pygame.K_RETURN:
                    if len(textBox.text) > 0:
                        #print (textBox.text)
                        running = False
                        

#image surfaces
free_hit = pygame.image.load(os.path.dirname(os.path.abspath(__file__))+'/frontend resources/free_hit_small.png')
free_hit_big = pygame.image.load(os.path.dirname(os.path.abspath(__file__))+'/frontend resources/free_hit_big.png')
sign_in = pygame.image.load(os.path.dirname(os.path.abspath(__file__))+'/frontend resources/sign_in.png')
sign_up = pygame.image.load(os.path.dirname(os.path.abspath(__file__))+'/frontend resources/sign_up.png')
knos_logo_image = pygame.image.load(os.path.dirname(os.path.abspath(__file__))+'/frontend resources/knos_logo.png')

#loading sounds
#click_sound = pygame.mixer.Sound(os.path.dirname(os.path.abspath(__file__))+'/frontend resources/click.wav')

#setting volume
#click_sound.set_volume(3)

#function for playing click sound
#def play_click_sound():
    #click_sound.play()
    # pygame.mixer.Sound.play(click_sound)
    # pygame.mixer.music.stop()
    
    

#game window name
pygame.display.set_caption('Free Hit')

#font to be used in the game
font = pygame.font.SysFont('arial', 25)

#colors to be used
red = (255,0,0)
white = (255,255,255)
black = (0,0,0)
grey = (200,200,200)
clock = pygame.time.Clock()

def knos_logo():
    gameDisplay = pygame.display.set_mode((display_width,display_height))
    gameDisplay.fill(white)
    gameDisplay.blit(knos_logo_image, (200, 50))
    pygame.display.update()
    time.sleep(4)


def free_hit_logo():
    gameDisplay = pygame.display.set_mode((display_width,display_height))
    gameDisplay.fill(white)
    gameDisplay.blit(free_hit_big, (200, 218))
    pygame.display.update()
    time.sleep(4)




# def free_hit_start():
#     font = pygame.font.Font(None, display_width//10)
#     text = font.render('FREE HIT', True, black)
#     textsec=text.copy()
#     alpha_surf = pygame.Surface(textsec.get_size(), pygame.SRCALPHA)
#     alpha = 255
#     textRect = text.get_rect()
#     textRect.center = (display_width // 2, display_height // 2)
#     while True:
#         if alpha > 0:
#             alpha = max(alpha-3, 0)
#             textsec=text.copy()
#             alpha_surf.fill((255, 255, 255, alpha))
#             textsec.blit(alpha_surf, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
#         else:
#             break
#         gameDisplay.fill(white)
#         gameDisplay.blit(textsec, textRect)
#         pygame.display.flip()
#         clock.tick(15)
 
#text function
def text_objects(text,color):
    textsurf = font.render(text,True,color)
    return textsurf,textsurf.get_rect()
#function for the text to be shown on button 

def text_to_button(text,color,button_x,button_y,button_width,button_height):
    textsurf, textrect = text_objects(text,color)
    #centering the text to button
    textrect.center = ((button_x+(button_width/2)),(button_y+(button_height/2)))
    gameDisplay.blit(textsurf,textrect)

#function for button (in this case "textual button")
def text_button(text,x,y,width,height,inactive_color,active_color,action,sound):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    
    if x + width > cur[0] > x and y + height > cur[1] > y:
        # play_click_sound()
        # test = pygame.mixer.get_num_channels()
        

        text_to_button(text,active_color,x,y,width,height)
        if click[0] == 1 and action != None and sound != None:
            if action == 'Sign In':
                sign_in_menu()
            elif action == 'Guest':
                guest_menu()
            elif action == 'Ok':
                After_succesful_signin_menu()
            elif action == 'Sign Up':
                sign_up_menu()
            elif action == 'Back':
                main_menu()
            elif action == 'Back from signup':
                main_menu()
            elif action == 'Exit':
                pygame.quit()
                quit()
            elif action == 'single player':
                Single_player_menu()
            elif action == 'Back to Guest Menu':
                guest_menu()
            elif action == 'Email':
                user_input()
            elif action == 'Pass':
                print('')
            
            # elif sound == 'Yes':
            #     play_click_sound()
            

                
                
            
            
    else:
        text_to_button(text,inactive_color,x,y,width,height)
        
        
#main menu for game
def main_menu():
    gameDisplay = pygame.display.set_mode((display_width,display_height))
    
    gamequit = False
    
    while not gamequit:
        
        gameDisplay.fill(white)
        gameDisplay.blit(free_hit, (250, 80))
        
#         pygame.draw.rect(gameDisplay, white, [350,150,100,25])
#         pygame.draw.rect(gameDisplay, white, [350,190,100,25])
#         pygame.draw.rect(gameDisplay, white, [350,230,100,25])
#         pygame.draw.rect(gameDisplay, white, [350,270,100,25])

        cur = pygame.mouse.get_pos()


        text_button("Sign In",350,180,100,25,black,red, action = 'Sign In',sound = 'Yes')
        text_button("Sign Up",350,220,100,25,black,red,action = 'Sign Up',sound = 'Yes')
        text_button("Guest",350,260,100,25,black,red,action = 'Guest',sound = 'Yes')
        text_button("Exit",350,300,100,25,black,red,action = 'Exit',sound = 'Yes')
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gamequit = True
                pygame.quit()
                quit()
            

#guest menu
def guest_menu():
    back  = False
    while not back:
        gameDisplay.fill(white) 
        
        gameDisplay.blit(free_hit, (250, 80))
        
#         pygame.draw.rect(gameDisplay, white, [350,150,100,25])
#         pygame.draw.rect(gameDisplay, white, [350,190,100,25])
#         pygame.draw.rect(gameDisplay, white, [350,230,100,25])
#         pygame.draw.rect(gameDisplay, white, [350,270,100,25])
#         pygame.draw.rect(gameDisplay, white, [350,310,100,25])
#         pygame.draw.rect(gameDisplay, white, [350,350,100,25])

        cur = pygame.mouse.get_pos()


        text_button("Single Player",350,180,100,25,black,red,action = None,sound = 'Yes' )
        text_button("Leaderboard",350,220,100,25,black,red,action = None,sound = 'Yes')
        text_button("Achievements",350,260,100,25,black,red,action = None,sound = 'Yes')
        text_button("Help",350,300,100,25,black,red,action = None,sound = 'Yes')
        text_button("Exit",350,340,100,25,black,red,action = 'Exit',sound = 'Yes')
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                back = True
                pygame.quit()
                quit()
    
#menu after clicking sign in option
def sign_in_menu():
    
    back  = False
    while not back:
        gameDisplay.fill(white) 
        
        gameDisplay.blit(sign_in, (275, 80))
        
#        pygame.draw.rect(gameDisplay, white, [350,150,100,25])
        pygame.draw.rect(gameDisplay, grey, [475,180,125,25])
        pygame.draw.rect(gameDisplay, grey, [475,1220,125,25])
#         pygame.draw.rect(gameDisplay, white, [350,190,100,25])
#         pygame.draw.rect(gameDisplay, white, [350,230,100,25])
#         pygame.draw.rect(gameDisplay, white, [350,270,100,25])

        cur = pygame.mouse.get_pos()


        text_button("Email",350,180,100,25,black,red,action = 'Email',sound = 'Yes' )
        text_button("Password",350,220,100,25,black,red,action = None,sound = 'Yes')
        text_button("Ok",350,260,100,25,black,red,action = 'Ok',sound = 'Yes')
        text_button("Back",350,300,100,25,black,red,action = 'Back',sound = 'Yes')

        
        

        pygame.display.update() 
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    back = True

#menu after clicking sign up option
def sign_up_menu():
    back  = False
    while not back:
        gameDisplay.fill(white) 
        
        gameDisplay.blit(sign_in, (263, 80))
        
#         pygame.draw.rect(gameDisplay, white, [350,150,100,25])
#         pygame.draw.rect(gameDisplay, white, [350,190,100,25])
#         pygame.draw.rect(gameDisplay, white, [350,230,100,25])
#         pygame.draw.rect(gameDisplay, white, [350,270,100,25])

        cur = pygame.mouse.get_pos()


        text_button("Email",350,180,100,25,black,red,action = None,sound = 'Yes' )
        text_button("Write Password",350,220,100,25,black,red,action = None,sound = 'Yes')
        text_button("Rewrite Password",350,260,100,25,black,red,action = None,sound = 'Yes')
        text_button("Back",350,300,100,25,black,red,action = 'Back from signup',sound = 'Yes')
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    back = True

#menu after successful sign in 
def After_succesful_signin_menu():
    back  = False
    while not back:
        gameDisplay.fill(white) 
        
        gameDisplay.blit(free_hit, (250, 80))
        
#         pygame.draw.rect(gameDisplay, white, [350,150,100,25])
#         pygame.draw.rect(gameDisplay, white, [350,190,100,25])
#         pygame.draw.rect(gameDisplay, white, [350,230,100,25])
#         pygame.draw.rect(gameDisplay, white, [350,270,100,25])
#         pygame.draw.rect(gameDisplay, white, [350,310,100,25])
#         pygame.draw.rect(gameDisplay, white, [350,350,100,25])

        cur = pygame.mouse.get_pos()


        text_button("Single Player",350,180,100,25,black,red,action = 'single player',sound = 'Yes' )
        text_button("Multiplayer",350,220,100,25,black,red,action = None,sound = 'Yes')
        text_button("Leaderboard",350,260,100,25,black,red,action = None,sound = 'Yes')
        text_button("Achievements",350,300,100,25,black,red,action = None,sound = 'Yes')
        text_button("Help",350,340,100,25,black,red,action = None,sound = 'Yes')
        text_button("Exit",350,380,100,25,black,red,action = 'Exit',sound = 'Yes')
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                back = True
                pygame.quit()
                quit()

#single player menu 
def Single_player_menu():
    back  = False
    while not back:
        gameDisplay.fill(white) 
        
        gameDisplay.blit(free_hit, (250, 80))
        
#         pygame.draw.rect(gameDisplay, white, [350,150,100,25])
#         pygame.draw.rect(gameDisplay, white, [350,190,100,25])
#         pygame.draw.rect(gameDisplay, white, [350,230,100,25])
#         pygame.draw.rect(gameDisplay, white, [350,270,100,25])
#         pygame.draw.rect(gameDisplay, white, [350,310,100,25])
#         pygame.draw.rect(gameDisplay, white, [350,350,100,25])

        cur = pygame.mouse.get_pos()


        text_button("Your Team",350,180,100,25,black,red,action = None,sound = 'Yes' )
        text_button("Opposite Team",350,220,100,25,black,red,action = None,sound = 'Yes')
        text_button("Overs",350,260,100,25,black,red,action = None,sound = 'Yes')
        text_button("Difficulty Level",350,300,100,25,black,red,action = None,sound = 'Yes')
        text_button("Start Game",350,380,100,25,black,red,action = None,sound = 'Yes')
        text_button("Back",350,420,100,25,black,red,action = 'Back to Guest Menu',sound = 'Yes')
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    back = True

gameexit = False
while not gameexit:
    
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameexit = True
    

    
    #free_hit_start()
    knos_logo()
    free_hit_logo()
    
    
    main_menu()
    
    
    
    
    
    
    
      


    
    

pygame.quit()
quit()
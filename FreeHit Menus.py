#importing necessary libraries
import pygame
import time

#intializing pygame
pygame.init()

#display dimensions
display_width = 800
display_height = 500

#display surface
gameDisplay = pygame.display.set_mode((display_width,display_height))

#image surfaces
free_hit = pygame.image.load(r'E:\free_hit_images\free_hit_small.png')
sign_in = pygame.image.load(r'E:\free_hit_images\sign_in.png')
sign_in = pygame.image.load(r'E:\free_hit_images\sign_up.png')

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
def text_button(text,x,y,width,height,inactive_color,active_color,action):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x + width > cur[0] > x and y + height > cur[1] > y:
        text_to_button(text,active_color,x,y,width,height)
        if click[0] == 1 and action != None:
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
            elif action == 'Email':
                print('')
            elif action == 'Pass':
                print('')
                
                
            
            
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


        text_button("Sign In",350,180,100,25,black,red, action = 'Sign In')
        text_button("Sign Up",350,220,100,25,black,red,action = 'Sign Up')
        text_button("Guest",350,260,100,25,black,red,action = 'Guest')
        text_button("Exit",350,300,100,25,black,red,action = 'Exit')
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


        text_button("Single Player",350,180,100,25,black,red,action = None )
        text_button("Leaderboard",350,220,100,25,black,red,action = None)
        text_button("Achievements",350,260,100,25,black,red,action = None)
        text_button("Help",350,300,100,25,black,red,action = None)
        text_button("Exit",350,340,100,25,black,red,action = 'Exit')
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


        text_button("Email",350,180,100,25,black,red,action = None )
        text_button("Password",350,220,100,25,black,red,action = None)
        text_button("Ok",350,260,100,25,black,red,action = 'Ok')
        text_button("Back",350,300,100,25,black,red,action = 'Back')
        

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


        text_button("Email",350,180,100,25,black,red,action = None )
        text_button("Write Password",350,220,100,25,black,red,action = None)
        text_button("Rewrite Password",350,260,100,25,black,red,action = None)
        text_button("Back",350,300,100,25,black,red,action = 'Back from signup')
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


        text_button("Single Player",350,180,100,25,black,red,action = None )
        text_button("Multiplayer",350,220,100,25,black,red,action = None)
        text_button("Leaderboard",350,260,100,25,black,red,action = None)
        text_button("Achievements",350,300,100,25,black,red,action = None)
        text_button("Help",350,340,100,25,black,red,action = None)
        text_button("Exit",350,380,100,25,black,red,action = 'Exit')
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                back = True
                pygame.quit()
                quit()

gameexit = False
while not gameexit:
    
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameexit = True
    

    
    
    
    main_menu()
    
    
    
    
    
    
    
      


    
    

pygame.quit()
quit()
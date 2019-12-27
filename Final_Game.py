import curses     
import sys                                                           
from curses import panel
from cursesmenu import *
from cursesmenu.items import *                                                     

class Menu(object):                                                          


    def __init__(self, items, stdscreen):                                    
        self.window = stdscreen.subwin(10,60)                               
        self.window.keypad(1)                                                
        self.panel = panel.new_panel(self.window)                            
        self.panel.hide()                                                    
        panel.update_panels()                                                

        self.position = 0                                                    
        self.items = items                                                   
        # self.items.append(('Exit','Exit'))                                   

    def navigate(self, n):                                                   
        self.position += n                                                   
        if self.position < 0:                                                
            self.position = 0                                                
        elif self.position >= len(self.items):                               
            self.position = len(self.items)-1                                

    def display(self):                                                       
        self.panel.top()                                                     
        self.panel.show()
        #self.panel.move(0,0)                                                    
        self.window.clear()                                                  

        while True:                                                          
            self.window.refresh()                                            
            curses.doupdate()                                                
            for index, item in enumerate(self.items):                        
                if index == self.position:                                   
                    mode = curses.A_REVERSE                                  
                else:                                                        
                    mode = curses.A_NORMAL                                   

                msg = '%s' % (item[0])                            
                self.window.addstr(1+index, 1, msg, mode)                    

            key = self.window.getch()                                        

            if key in [curses.KEY_ENTER, ord('\n')]:                         
                if self.position == len(self.items)-1:                       
                    break                                                    
                else:                                                        
                    self.items[self.position][1]()                           

            elif key == curses.KEY_UP:                                       
                self.navigate(-1)                                            

            elif key == curses.KEY_DOWN:                                     
                self.navigate(1)                                             

        self.window.clear()                                                  
        self.panel.hide()                                                    
        panel.update_panels()                                                
        curses.doupdate()

        

class MyApp(object):                                                         

    def __init__(self, stdscreen):                                           
        self.screen = stdscreen                                              
        curses.curs_set(0)

        # Single Player Menu Bar
        Single_Player_submenu_items= [ 
                ('   Your Team :      < Pakistan   >', curses.flash),
                (' Opposite Team:     < Sri Lanka  >', curses.flash),
                ('    Overs :         < 10         >', curses.flash),
                ('Difficulty Level:   < Expert     >', curses.flash),
                ('                                  ', curses.flash),
                ('            Start Game:           ', curses.flash),
                ('               Back               ', curses.beep)                                     
                ]                                                            
        submenu_Single_Player = Menu(Single_Player_submenu_items, self.screen)


        #Multiplayer sub Menu BAr 1

        Multiplayer1_submenu_items = [
                ('Enter Player ID: ',curses.flash), 
                ('                 ', curses.flash),
                ('                 ', curses.flash),
                ('                 ', curses.flash), 
                ('   Start Game:  ', curses.flash),
                ('      Back       ', curses.beep)                                          
                ]                                               
        submenu_Multiplayer1 = Menu(Multiplayer1_submenu_items, self.screen)

         #Multiplayer sub Menu BAr 2

        Multiplayer2_submenu_items = [
                ('   Start Game:  ', curses.flash),
                ('      Back       ', curses.beep)                                        
                ]                                               
        submenu_Multiplayer2 = Menu(Multiplayer2_submenu_items, self.screen)


        #Multiplayer Menu BAr

        Multiplayer_submenu_items = [
                ('Play with a Friend: ',submenu_Multiplayer1.display),         
                ('Find a Match:', submenu_Multiplayer2),
                ('Back', curses.beep)                                           
                ]                                               
        submenu_Multiplayer = Menu(Multiplayer_submenu_items, self.screen)
        

         #Help

        Help_submenu_items = [
                ('Control ',curses.flash),  
                ('About   ',curses.flash),        
                ('Contact ',curses.flash),
                ('Back    ', curses.beep)                                           
                ]                                               
        submenu_Help = Menu(Help_submenu_items, self.screen)


         # start menu after entering you id and password
 
        Start_Menu_submenu_items = [
                ("Single Player",submenu_Single_Player.display),
                (" Multiplayer",submenu_Multiplayer.display),
                ("    Help",submenu_Help.display),
                ("Leader Board",curses.flash),
                ("Achievements",curses.flash),
                ("    Exit",curses.flash)                            
                ]                                               
        submenu_Start_Menu = Menu(Start_Menu_submenu_items, self.screen)




       # Sign In Option

        SignIn_submenu_items = [                                                    
                ('Player ID: ', curses.flash),                                       
                ('Password: ', curses.flash),
                ('OK', submenu_Start_Menu.display),
                ('Back', curses.beep)                                   
                ]                                                            
        submenu_SignIn = Menu(SignIn_submenu_items, self.screen)                           


      # Sign Up Option 
      #   
        SignUp_submenu_items = [
                ('Name: ',curses.flash),                                
                ('Email: ', curses.flash),                      
                ('Password: ', curses.flash),
                ('OK', submenu_Start_Menu.display),
                ('Back', curses.beep)                      
                ]                                               
        submenu_SignUp = Menu(SignUp_submenu_items, self.screen)


      # first Menu Occur On the Screen...

        main_menu_items = [                                                  
                ('Sign In', submenu_SignIn.display),                                       
                ('Sign Up', submenu_SignUp.display),                               
                ('Guest', curses.beep),
                ('Exit',)                                 
                ]                                                            
        main_menu = Menu(main_menu_items, self.screen)                       
        main_menu.display()                                                  

if __name__ == '__main__':                                                       
    curses.wrapper(MyApp)
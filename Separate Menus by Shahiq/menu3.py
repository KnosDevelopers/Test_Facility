import curses                                                                
from curses import panel                                                     

class Menu(object):                                                          

    def __init__(self, items, stdscreen):                                    
        self.window = stdscreen.subwin(0,0)                                  
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
        self.panel.move(0,0)                                                    
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
                                                   

        SignIn_submenu_items = [                                                    
                ('Email: ', curses.flash),                                       
                ('Password: ', curses.flash),
                ('OK', curses.beep),
                ('Back',)                                      
                ]                                                            
        submenu_SignIn = Menu(SignIn_submenu_items, self.screen)                           

        SignUp_submenu_items = [
                ('Name: ',curses.flash),                                
                ('Email: ', curses.flash),                      
                ('Password: ', curses.flash)                    
                ]                                               
        submenu_SignUp = Menu(SignUp_submenu_items, self.screen)

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
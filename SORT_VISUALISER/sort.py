import pygame as pg
import random
import time

import algoritms 

size=[1000,500]

class Main:
    def __init__(self):
        pg.init()
        self.screen=pg.display.set_mode((size[0],size[1]))
        font = pg.font.SysFont(None, 40)
        
        self.data=self.data_pick()
        tools=Tools(self)
        options=Options(self.screen,algoritms.algorithms,font)
        sort_visualiser=Sort_Visualiser(self.screen,self.data,options,tools)
        
        
        running=True
        while running==True:
            for event in pg.event.get():
                if event.type==pg.QUIT:
                    running=False
            self.screen.fill((0,0,0))
            
            tools.reset()
            sort_visualiser.draw() 
            options.draw()  

            options.move(sort_visualiser)
                        
            pg.display.update()
            
    def data_pick(self):
        data=[]
        for i in range(80):
            data.append(random.randrange(1,100))
        return data
        
class Sort_Visualiser:
    def __init__(self,screen,data,options,tools):
        self.tools=tools
        self.options=options
        self.screen=screen
        self.maximum=max(data)
        self.data=data
        
        info = pg.display.Info()
        self.screen_width = info.current_w
        self.screen_height = info.current_h

    def draw(self,swap_1=-1,swap_2=-1,pivot=-1):
        
        self.screen.fill((0,0,0))
        for i in range(len(self.data)):
            
            thickness=self.screen_width/5*4/len(self.data)
            x=self.screen_width/5+i*thickness
            y=50+((self.screen_height-50)/self.maximum)*(self.maximum-self.data[i])
            heightness=self.screen_height-y
            if i==swap_1:
                pg.draw.rect(self.screen,(255,0,0),(x,y,thickness-1,heightness))
            elif i==swap_2:
                pg.draw.rect(self.screen,(0,255,0),(x,y,thickness-1,heightness))
            elif i==pivot:
                pg.draw.rect(self.screen,(255,0,255),(x,y,thickness-1,heightness))
            else:
                pg.draw.rect(self.screen,(0,0,255),(x,y,thickness-1,heightness))
        self.tools.reset()
        self.options.draw()
        self.options.move(self)
        time.sleep(0.01)
        pg.display.update()
        
    def sort(self,sorting):
        sorting(self.data,self.draw)
                          
class Options:
    def __init__(self,screen,algoritms,font):
        self.scroll=0
        self.screen=screen
        self.font=font
        
        info = pg.display.Info()
        self.screen_width = info.current_w
        self.screen_height = info.current_h
        
        self.algoritms=algoritms
    
    def draw(self):
        for algo in range(len(self.algoritms)):
            x=0
            thickness=self.screen_width/5
            heightness=self.screen_height/5
            y=heightness*algo-self.scroll
            pg.draw.rect(self.screen,(10,12,55),(x,y,thickness,heightness-1))
            text=self.font.render(list(self.algoritms.keys())[algo],True,(255,255,255))
            self.screen.blit(text,(x+30,y+40))
                
    def move(self,sort_visualiser):
        for event in pg.event.get():  
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 5 and self.scroll<len(algoritms.algorithms)/5*self.screen_height-self.screen_height:  # Scroll up
                    self.scroll += 30
                elif event.button == 4 and self.scroll>0:  # Scroll down
                    self.scroll -= 30
            if event.type == pg.MOUSEBUTTONDOWN and event.button==1:
                positions=pg.mouse.get_pos()
                for algo in range(len(self.algoritms)):
                    thickness=self.screen_width/5
                    heightness=self.screen_height/5
                    y=heightness*algo-self.scroll
                    if positions[0]>0 and positions[0]<thickness and positions[1]>y and positions[1]<y+heightness:
                        sort_visualiser.sort(list(self.algoritms.values())[algo])
   
class Tools:
    def __init__(self,main):
        self.main=main
        info = pg.display.Info()
        self.screen_width = info.current_w
        self.screen_height = info.current_h
    
    def reset(self):
        rectangle=(self.screen_width/5*1,0,70,70)
        pg.draw.rect(self.main.screen,(100,0,100),rectangle)
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN and event.button==1:
                position=pg.mouse.get_pos()
                if position[0]>rectangle[0] and position[0]<rectangle[0]+rectangle[2] and position[1]>rectangle[1] and position[1]<rectangle[1]+rectangle[3]:
                    self.main.data=self.main.data_pick()
                    print('a')
        
   
   
        
Main()

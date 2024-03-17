import pygame as pg
import random
import time

import algoritms

size = [1000, 500]


class PyGameGUI:
    def __init__(self):
        self.screen = pg.display.set_mode((size[0], size[1]))
        self.info = pg.display.Info()
        self.font = pg.font.SysFont(None, 40)

        self.data = self.data_pick()
        self.sort_visualiser = SortVisualiser(self, self.data)
        self.tools = Tools(self)
        self.options = Options(self)
        self.running = True
        self.clock_tick=60

    def run(self):
        clock = pg.time.Clock()
        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                self.tools.reset_event(event)
                self.tools.stop_event(event)
                self.tools.speed_event(event)
                self.options.reset_event(event)
            self.screen.fill((0, 0, 0))

            self.sort_visualiser.draw()
            self.options.draw()
            self.tools.draw()

            pg.display.update()
            clock.tick(self.clock_tick)  # limits FPS to 60

    def data_pick(self):
        data = []
        for i in range(50):
            data.append(random.randrange(1, 100))
        return data

    def reset_data(self):
        self.data = self.data_pick()
        self.sort_visualiser.data = self.data
        self.sort_visualiser.sorted=None
        
    def stop(self):
        self.sort_visualiser.sorted=None


class SortVisualiser:
    def __init__(self, main_gui, data):
        self.main_gui = main_gui
        self.maximum = max(data)
        self.data = data
        self.sorted = None

    def draw(self, swap_1=-1, swap_2=-1, pivot=-1):
        screen_width = self.main_gui.info.current_w
        screen_height = self.main_gui.info.current_h
        
        if self.sorted is not None:
            try:
                swap_1, swap_2 = next(self.sorted)
            except StopIteration:
                self.sorted = None
            
        for i in range(len(self.data)):
            thickness = screen_width / 5 * 4 / len(self.data)
            x = screen_width / 5 + i * thickness
            y = 50 + ((screen_height - 50) / self.maximum) * (
                self.maximum - self.data[i]
            )
            heightness = screen_height - y
            if i == swap_1:
                pg.draw.rect(
                    self.main_gui.screen,
                    (255, 0, 0),
                    (x, y, thickness - 1, heightness),
                )
            elif i == swap_2:
                pg.draw.rect(
                    self.main_gui.screen,
                    (0, 255, 0),
                    (x, y, thickness - 1, heightness),
                )
            elif i == pivot:
                pg.draw.rect(
                    self.main_gui.screen,
                    (255, 0, 255),
                    (x, y, thickness - 1, heightness),
                )
            else:
                pg.draw.rect(
                    self.main_gui.screen,
                    (0, 0, 255),
                    (x, y, thickness - 1, heightness),
                )        
                
    def reset_sorting(self, algorithm):
        self.sorted = algorithm(self.data)



class Options:
    def __init__(self, main_gui):
        # drawing configuration
        self.main_gui = main_gui
        self.screen_width = self.main_gui.info.current_w
        self.screen_height = self.main_gui.info.current_h
        self.algoritms = algoritms.algorithms
        self.scroll = 0

    def draw(self):
        for algo in range(len(self.algoritms)):
            x = 0
            thickness = self.main_gui.info.current_w / 5
            heightness = self.main_gui.info.current_h / 5
            y = heightness * algo - self.scroll
            pg.draw.rect(
                self.main_gui.screen, (10, 12, 55), (x, y, thickness, heightness - 1)
            )
            text = self.main_gui.font.render(
                list(self.algoritms.keys())[algo], True, (255, 255, 255)
            )
            self.main_gui.screen.blit(text, (x + 30, y + 40))

    def reset_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if (
                event.button == 5
                and self.scroll
                < len(algoritms.algorithms) / 5 * self.screen_height
                - self.screen_height
            ):  # Scroll up
                self.scroll += 30
            elif event.button == 4 and self.scroll > 0:  # Scroll down
                self.scroll -= 30
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            positions = pg.mouse.get_pos()
            for algo in range(len(self.algoritms)):
                thickness = self.screen_width / 5
                heightness = self.screen_height / 5
                y = heightness * algo - self.scroll
                if (
                    positions[0] > 0
                    and positions[0] < thickness
                    and positions[1] > y
                    and positions[1] < y + heightness
                ):
                    self.main_gui.sort_visualiser.reset_sorting(list(
                        self.algoritms.values()
                    )[algo])


class Tools:
    def __init__(self, main_gui):
        self.main_gui = main_gui
        self.reset_rectangle = (main_gui.info.current_w / 5 * 1, 0, 70, 70)
        self.stop_rectangle =(main_gui.info.current_w / 5 * 1+70, 0, 70, 70)
        self.speed_rectangle=(main_gui.info.current_w / 5 * 1+140, 0, 210, 70)
        self.point=[main_gui.info.current_w / 5 * 1+160,35]
        self.stop_image = pg.transform.scale(pg.image.load("SORT_VISUALISER\stop_icon.png"), (70,70))
        self.reset_image = pg.transform.scale(pg.image.load("SORT_VISUALISER\\reset.png"), (70,70))

    def draw(self):
        rect=pg.Rect(self.reset_rectangle)
        self.main_gui.screen.blit(self.reset_image, rect)
        rect=pg.Rect(self.stop_rectangle)
        self.main_gui.screen.blit(self.stop_image, self.stop_rectangle)
        pg.draw.rect(self.main_gui.screen, (0,0,150), self.speed_rectangle)
        pg.draw.rect(self.main_gui.screen, (0,0,100), (self.main_gui.info.current_w / 5 * 1+155,30,180,10))
        pg.draw.circle(self.main_gui.screen, (0,0,255),self.point,10)

    def reset_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            position = pg.mouse.get_pos()
            if (
                position[0] > self.reset_rectangle[0]
                and position[0] < self.reset_rectangle[0] + self.reset_rectangle[2]
                and position[1] > self.reset_rectangle[1]
                and position[1] < self.reset_rectangle[1] + self.reset_rectangle[3]
            ):
                self.main_gui.reset_data()
                
    def stop_event(self,event):
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            position = pg.mouse.get_pos()
            if (
                position[0] > self.stop_rectangle[0]
                and position[0] < self.stop_rectangle[0] + self.stop_rectangle[2]
                and position[1] > self.stop_rectangle[1]
                and position[1] < self.stop_rectangle[1] + self.stop_rectangle[3]
            ):
                self.main_gui.stop()
    def speed_event(self,event):
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            position = pg.mouse.get_pos()
            if (
                position[0] > self.point[0]-15
                and position[0] < self.point[0] + 15
                and position[1] > self.point[1]-15
                and position[1] < self.point[1]+15
                and position[0] > self.speed_rectangle[0]+20
                and position[0] < self.speed_rectangle[0] + self.speed_rectangle[2]-20
            ):
                self.point[0]=position[0]
        if pg.mouse.get_pressed()[0]:
            position = pg.mouse.get_pos()
            if (
                position[0] > self.speed_rectangle[0]+20
                and position[0] < self.speed_rectangle[0] + self.speed_rectangle[2]-20
            ):
                self.point[0]=position[0]
        self.main_gui.clock_tick=self.point[0]-330
        


if __name__ == "__main__":
    pg.init()

    gui = PyGameGUI()
    gui.run()
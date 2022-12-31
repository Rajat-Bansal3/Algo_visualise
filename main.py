import pygame
import random
import math

pygame.init()



class info:
    SIDE_PAD = 100
    TOP_PAD = 150
    
    
    WHITE = 255 , 255 , 255
    BLACK = 0 , 0 , 0
    RED = 255 , 255 , 255
    GREEN = 0 , 255 , 0
    GREY = 125 , 125 , 125
    BG_COLOR = WHITE

    GRADIENTS = [
        (128, 128, 128),
		(160, 160, 160),
		(192, 192, 192)
    ]

    def __init__(self,width,height,lst) :
        self.height = height
        self.width = width

        self.window = pygame.display.set_mode((width,height))
        pygame.display.set_caption("visalgo")
        self.setlist(lst)

    def setlist(self , lst):
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)

        self.block_width = round(( self.width - self.SIDE_PAD ) / len(lst))
        self.block_height = round(( self.height - self.TOP_PAD ) / (self.max_val - self.min_val))
        self.stx = self.SIDE_PAD // 2



def draw(info):
    info.window.fill(info.BG_COLOR)
    draw_list(info)
    pygame.display.update()



def draw_list(info):
    lst  = info.lst
    for i ,val in enumerate(lst):
        x = info.stx + i * info.block_width
        y = info.height - (val - info.min_val) * info.block_height

        color = info.GRADIENTS[ i % 3 ]
        pygame.draw.rect(info.window,color , (x , y , info.block_width , info.height ))



def st_lst(a , min_val , max_val):
    lst = []

    for i in range(a):
        lst.append(random.randint(min_val,max_val))

    return lst



def main():
    y = True
    clock = pygame.time.Clock()
    
    a = 50
    min_val = 0
    max_val = 200

    lst = st_lst(a , min_val , max_val)
    drawinfo = info(800,600,lst)
    
    while y :
        clock.tick(120)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                y = False
            if event.type != pygame.KEYDOWN:
                continue
            # if event.key == pygame.K_r:
            #     gt = st_lst(a , min_val , max_val)
            #     info.setlist(gt)###### whyyyyyyyy tf what the fk !_! keray aa rha h frens ###### 
            
            
            if event.key == pygame.K_ESCAPE:
                y = False
                

        draw(drawinfo)
    
    pygame.quit()



if __name__ == "__main__":
    main()

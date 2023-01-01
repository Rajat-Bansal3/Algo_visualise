import pygame
import random
import math

pygame.init()



class info:
    SIDE_PAD = 100
    TOP_PAD = 150
    
    FONT = pygame.font.Font("S:\FONTS\GothicJoker-gxxGP.ttf",25)
    LARGEFONT = pygame.font.SysFont('Segoe UI',50,bold=True,italic=True)

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
    
    txt = info.FONT.render("R->Reset || A->ascending || D->Descending || ESC->Quit || SPACE->Start Sorting",5,info.BLACK,)
    info.window.blit(txt,((info.width/2 - txt.get_width()/2),5))
    
    _txt = info.FONT.render("B->Bubble Sort || I->Insertion Sort",5,info.BLACK,)
    info.window.blit(_txt,((info.width/2 - _txt.get_width()/2),35))

    pygame.display.update()

def draw_list(info , color_pos = {} , clear_bg = False):
    lst  = info.lst

    if clear_bg:
        clear_rect = (info.SIDE_PAD//2 , info.TOP_PAD,info.width - info.SIDE_PAD , info.HEIGHT - info.TOP_PAD )
        pygame.draw.rect(info.window,info.BG_COLOR,clear_rect)

    if clear_bg:
        pygame.display.update()
        

    for i ,val in enumerate(lst):
        x = info.stx + i * info.block_width
        y = info.height - (val - info.min_val) * info.block_height

        color = info.GRADIENTS[ i % 3 ]
        
        if i in color_pos:
            color = color_pos[i] 
        
        pygame.draw.rect(info.window,color , (x , y , info.block_width , info.height ))



def st_lst(a , min_val , max_val):
    lst = []

    for i in range(a):
        lst.append(random.randint(min_val,max_val))

    return lst

def bubble(info , ascending = True):
    lst = info.lst

    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            num1 = lst[j]
            num2 = lst[j + 1]

            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                num1 , num2 = num2 , num1
                draw_list(info,{j:info.GREEN,j+1:info.RED})
                yield True
    return lst

def insertion():
    pass




def main():
    y = True
    clock = pygame.time.Clock()
    
    a = 50
    min_val = 0
    max_val = 200

    sorting = False
    ascending = True
    sorting_algorithm = bubble
    sorting_algo_name = "Bubble"
    sorting_algorithm_generator = None

    lst = st_lst(a , min_val , max_val)
    drawinfo = info(800,600,lst)
    
    while y :
        clock.tick(120)

        if sorting:
            try:
                next(sorting_algorithm_generator)
            except StopIteration:
                sorting = False
		
        else:
            draw(drawinfo)

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                y = False
            if event.type != pygame.KEYDOWN:
                continue
            if event.key == pygame.K_r:
                list = st_lst(a,min_val,max_val)
                drawinfo.setlist(lst=list)
                sorting = False

            
            elif event.key == pygame.K_SPACE and sorting == False:
                sorting = True
            

            elif event.key == pygame.K_a and sorting == False:
                ascending = True
                sorting_algorithm_generator = sorting_algorithm(info, ascending)


            elif event.key == pygame.K_d and sorting == False:
                ascending = False


            elif event.key == pygame.K_ESCAPE and sorting == False:
                y = False


        draw(drawinfo)

    
    pygame.quit()


if __name__ == "__main__":
    main()

import pygame
import random


'initialised window'
pygame.init()


'class to store value'
class info:
    SIDE_PAD = 50
    TOP_PAD = 150
    
    FONT = pygame.font.Font("S:\FONTS\GothicJoker-gxxGP.ttf",25)
    LARGEFONT = pygame.font.SysFont('S:\FONTS\GothicJoker-gxxGP.ttf',35,bold=False,italic=True)

    WHITE = 255 , 255 , 255
    BLACK = 0 , 0 , 0
    RED = 255 , 0 , 0
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

    "making the dimension and setting offsets of list px's"
    def setlist(self , lst):
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)

        self.block_width = round(( self.width - self.SIDE_PAD ) / len(lst))
        self.block_height = round(( self.height - self.TOP_PAD ) / (self.max_val - self.min_val))
        self.stx = self.SIDE_PAD // 2


'drawing canvas and rendering all the text elements'
def draw(info,algoname,ascending):

    info.window.fill(info.BLACK)

    draw_list(info)

    op = "ascending" if ascending else "descending"
    a = "{}-{}".format(algoname,op)

    __txt = info.LARGEFONT.render(a,5,info.GREEN,)
    info.window.blit(__txt,((info.width/2 - __txt.get_width()/2),5))

    txt = info.FONT.render("R->Reset || A->ascending || D->Descending || ESC->Quit || SPACE->Start Sorting",5,info.GREEN,)
    info.window.blit(txt,((info.width/2 - txt.get_width()/2),40))
    
    _txt = info.FONT.render("B->Bubble Sort || I->Insertion Sort",5,info.GREEN,)
    info.window.blit(_txt,((info.width/2 - _txt.get_width()/2),70))

    pygame.display.update()


'drawing list bases on offsets'
def draw_list(drawinfo , color_pos = {} , clear_bg = False):

    lst  = drawinfo.lst
    
    if clear_bg:
        clear_rect = (drawinfo.SIDE_PAD//2 , drawinfo.TOP_PAD,drawinfo.width - drawinfo.SIDE_PAD , drawinfo.height - drawinfo.TOP_PAD )
        pygame.draw.rect(drawinfo.window,drawinfo.BG_COLOR,clear_rect)

    if clear_bg:
        pygame.display.update()

    for i ,val in enumerate(lst):

        x = drawinfo.stx + i * drawinfo.block_width
        y = drawinfo.height - (val - drawinfo.min_val) * drawinfo.block_height

        color = drawinfo.GRADIENTS[i % 3]

        if i in color_pos:
            color = color_pos[i]
            print(i)#comment out if u need no output in terminal i did this for my own refference of indexing swaps and insertions points
        
        pygame.draw.rect(drawinfo.window,color , (x , y , drawinfo.block_width , drawinfo.height ))


'starting random list generator'
def st_lst(a , min_val , max_val):
    lst = []

    for i in range(a):
        lst.append(random.randint(min_val,max_val))

    return lst


'bubble sort algo gen'
def bubble(drawinfo , ascending = True):
    lst = drawinfo.lst

    t = 0

    for i in range(len(lst)-1,0,-1):
        for j in range(i):
            num1 = lst[j]
            num2 = lst[j+1]
            
            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                if lst[j]>lst[j+1]:
                    t = lst[j]
                    lst[j] = lst[j+1]
                    lst[j+1] = t
                   
                    draw_list(drawinfo,color_pos={j:drawinfo.RED,j+1:drawinfo.GREEN},clear_bg=False)
                    print(j)
                   
                    yield True
                
                
                else:
                    t = lst[j+1]
                    lst[j+1] = lst[j]
                    lst[j] = t
                    
                    draw_list(drawinfo,color_pos={j:drawinfo.RED,j+1:drawinfo.GREEN},clear_bg=False)
                    print(j)
                    
                    yield True
                
    return lst

'insertion sort algorithm gen'
def insertion(drawinfo, ascending=True):
	lst = drawinfo.lst

	for i in range(1, len(lst)):
		current = lst[i]

		while True:
			ascending_sort = i > 0 and lst[i - 1] > current and ascending
			descending_sort = i > 0 and lst[i - 1] < current and not ascending

			if not ascending_sort and not descending_sort:
				break

			lst[i] = lst[i - 1]
			i = i - 1
			lst[i] = current

			draw_list(drawinfo, {i - 1: drawinfo.GREEN, i: drawinfo.RED}, False)

			yield True

	return lst
                

'main function with variables and class called'
def main():

    y = True
    clock = pygame.time.Clock()
    
    a = 150
    min_val = 0
    max_val = 100

    sorting = False
    ascending = True
    
    sorting_algorithm = bubble
    sorting_algo_name = "Bubble Sort"
    sorting_algorithm_generator = None

    lst = st_lst(a , min_val , max_val)
    drawinfo = info(800,600,lst)
    
    while y :

        clock.tick(128)#set tick rate accordingly and comment out this whole line for fastest execution or visualisation
       
       
        'generator iterator'
        if sorting:
            try:
                next(sorting_algorithm_generator)
            except StopIteration:
                sorting = False
		
        else:
            draw(drawinfo,sorting_algo_name,ascending)

        
        'defining events'
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
                sorting_algorithm_generator = sorting_algorithm(drawinfo , ascending )
            

            elif event.key == pygame.K_a and sorting == False:
                ascending = True


            elif event.key == pygame.K_d and sorting == False:
                ascending = False
            

            elif event.key == pygame.K_b :
                sorting_algo_name = "Bubble Sort"
                sorting_algorithm = bubble
            

            elif event.key == pygame.K_i :
                sorting_algo_name = "Insertion Sort"
                sorting_algorithm = insertion


            elif event.key == pygame.K_ESCAPE and sorting == False:
                y = False


        'initial draw on canvas'
        draw(drawinfo,sorting_algo_name,ascending)

    
    pygame.quit()


if __name__ == "__main__":
    main()

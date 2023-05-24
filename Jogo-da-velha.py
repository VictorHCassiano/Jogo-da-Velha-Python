import pygame 
from pygame.locals import *

pygame.init()

altura_tela = 300
largura_tela = 300
marcas = []
click= False
pos = []
player = 1
ganhador = 0
game_over = False




tela = pygame.display.set_mode((altura_tela,largura_tela))
pygame.display.set_caption('JogodaVelha')


verde = (0,255,0)
vermelho = (255,0,0)
azul = (0,0,255)
font = pygame.font.SysFont(None,40)

linha_largura=4

def draw_grid():
    bg = (255,255,200)
    grid = (50,50,50)
    tela.fill(bg)
    for x in range(1,3):
        pygame.draw.line(tela,grid, (0,x*100), (largura_tela,x*100),linha_largura)
        pygame.draw.line(tela,grid, (x*100,0), (x*100,altura_tela),linha_largura)

for x in range(3):
    linha = [0] * 3
    marcas.append(linha)



def draw_marcas():
        x_pos = 0
        for x in marcas:
             y_pos = 0
             for y in x:
                  if y == 1:
                       pygame.draw.line(tela,vermelho,(x_pos * 100 + 15 , y_pos * 100 + 15), (x_pos*100 + 85 , y_pos * 100 + 85), linha_largura)
                       pygame.draw.line(tela,vermelho,(x_pos * 100 + 15 , y_pos * 100 + 85), (x_pos*100 + 85 , y_pos * 100 + 15), linha_largura)
                  if y == -1:
                       pygame.draw.circle(tela,verde,(x_pos * 100 + 50, y_pos * 100 + 50 ), 38 , linha_largura)
                  y_pos += 1
             x_pos +=1


def check_winner():
     
    global ganhador
    global game_over


    y_pos = 0
    for x in marcas:
         if sum(x) == 3:
              ganhador = 1
              game_over = True
         if sum(x) == -3:
              ganhador = 1
              game_over = True
         if marcas[0][y_pos] + marcas[1][y_pos] + marcas[2][y_pos] == 3:
              ganhador = 1
              game_over = True
         if marcas[0][y_pos] + marcas[1][y_pos] + marcas[2][y_pos] == -3:
              ganhador = 2
              game_over = True
         y_pos +=1
    if marcas[0][0] + marcas[1][1] + marcas[2][2] == 3 or marcas[2][0] + marcas[1][1] + marcas[0][2] == 3:
         ganhador = 1
         game_over = True
    if marcas[0][0] + marcas[1][1] + marcas[2][2] == -3 or marcas[2][0] + marcas[1][1] + marcas[0][2] == -3:
         ganhador = 2
         game_over = True


def draw_ganhador(ganhador):
    win_text = 'Player ' + str(ganhador) + " ganhou!!!"
    win_img = font.render(win_text,True,azul)
    pygame.draw.rect(tela,verde,(largura_tela // 2 - 100, altura_tela // 2 - 60 , 200 , 50))
    tela.blit(win_img, (largura_tela // 2 - 100,altura_tela // 2 - 50 ))


run = True
while run:
    draw_grid()
    draw_marcas()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if game_over == 0:
            if event.type == pygame.MOUSEBUTTONDOWN and click == False:
                click= True
            if event.type == pygame.MOUSEBUTTONUP and click == True:
                click = False
                pos = pygame.mouse.get_pos()
                cell_x = pos[0]
                cell_y = pos[1]
                if marcas[cell_x // 100][cell_y // 100] == 0:
                        marcas[cell_x // 100][cell_y // 100] = player
                        player *= -1
                        check_winner()

    if game_over == True:
        draw_ganhador(ganhador)





    pygame.display.update()
pygame.quit()
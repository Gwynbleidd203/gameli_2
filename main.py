import pygame

from typing import Literal

# Init

pygame.init()
pygame.font.init()

# Janela
display = pygame.display.set_mode((1280, 720))

#3 Parte - formas - player
#pos e forma em retangulo
# 0,0 pos esquerda superior
#player1 = pygame.Rect(0, 0, 30, 150)
player1_img = pygame.image.load("assets/player1.png")
player1 = player1_img.get_rect()
player1_velocidade = 6
player1_score = 0


#player2 = pygame.Rect(1250, 0, 30, 150)
player2_img = pygame.image.load("assets/player2.png")
player2 = player2_img.get_rect(right=1280)
player2_score = 0

#ball = pygame.Rect(600, 350, 15, 15)
ball_img = pygame.image.load("assets/ball.png")
ball = ball_img.get_rect(center=[1280 / 2, 720 / 2])

campo_img = pygame.image.load("assets/bg.png")
campo = campo_img.get_rect()

ball_dir_x, ball_dir_y = 6, 6

# Placar

font = pygame.font.Font(None, 50)

placar_player1 = font.render(str(player1_score), True, "white")
placar_player2 = font.render(str(player2_score), True, "white")


menu_img = pygame.image.load("assets/menu.png")
menu = menu_img.get_rect()

gameover_img = pygame.image.load("assets/gameover.png")
gameover = menu_img.get_rect()

fade_img = pygame.Surface((1280, 720)).convert_alpha()
fade = fade_img.get_rect()
fade_img.fill("black")
fade_alpha = 255

music = pygame.mixer.Sound("assets/music.ogg")
music.play(-1)

def redirect_ball(axis:Literal["x", "y"]):

    if axis == "x":

        ball.x = 600
        ball_dir_x *= -1

    if axis == "y":

        ball_dir_y *= -1


#loop do game

cena:Literal["menu", "jogo", "gameover"] = "menu"

fps = pygame.time.Clock()

loop = True

while loop:

    if cena == "jogo":

        #Parte 2 - eventos
        for event in pygame.event.get():
            #evento do X de fechar
            if event.type == pygame.QUIT:
                loop = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:

                    player1_velocidade = 6

                if event.key == pygame.K_w:

                    player1_velocidade -= 6

                if event.key == pygame.K_SPACE:

                    player1.height += 50

                if event.key == pygame.K_0:

                    player2.height -= 10

        if player2_score >= 3 or player1_score >= 3:

            cena = "gameover"

            fade_alpha = 255

        #parte 6 - colisão e mov bola

        if ball.colliderect(player1) or ball.colliderect(player2):

            hit = pygame.mixer.Sound('assets/pong.wav')
            hit.play()

            ball_dir_x *= -1

        if player1.y <= 0:

            player1.y = 0

        elif player1.y >= 720-150:

            player1.y = 720 - 150

        player1.y += player1_velocidade

        if ball.x <= 0:

            player2_score += 1
            placar_player2 = font.render(str(player2_score), True, "white")

            ball.x = 600
            ball_dir_x *= -1

        elif ball.x >= 1280:

            player1_score += 1
            placar_player1 = font.render(str(player1_score), True, "white")

            ball.x = 600
            ball_dir_x *= -1

        if ball.y <= 0:

            ball_dir_y *= -1

        elif ball.y >= 720 - 15:

            ball_dir_y *= -1

        ball.x += ball_dir_x
        ball.y += ball_dir_y

        player2.y = ball.y - 75

        #fica preenchendo a tela

        display.fill((0, 0, 0))

        display.blit(campo_img, campo)

        
        display.blit(player1_img, player1)
        
        display.blit(player2_img, player2)
        display.blit(ball_img, ball)

        display.blit(placar_player1, (500, 50))
        display.blit(placar_player2, (780, 50))

    elif cena == "gameover":

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                loop = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN:

                    player1_score = 0
                    player2_score = 0

                    placar_player1 = font.render(str(player1_score), True, "white")

                    placar_player2 = font.render(str(player2_score), True, "white")

                    ball.x = 640
                    ball.y = 320

                    player1.y, player2.y = 0, 0

                    cena = "menu"

                    fade_alpha = 255

                    if event.key == pygame.K_q:

                        loop = False

        if fade_alpha > 0:

            fade_alpha -= 10
            fade_img.set_alpha(fade_alpha)


        display.fill((0, 0, 0))
        display.blit(gameover_img, gameover)
        display.blit(fade_img, fade)

    elif cena == "menu":

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                loop = False
            
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN:

                    cena = "jogo"

                    fade_alpha = 255

                    start = pygame.mixer.Sound("assets/start.wav")
                    start.play()

                if event.key == pygame.K_q:

                    loop = False

        if fade_alpha > 0:

            fade_alpha -= 10
            fade_img.set_alpha(fade_alpha)

        display.fill((0, 0, 0))
        display.blit(menu_img, menu)
        display.blit(fade_img, fade)

    fps.tick(60)

    #atualizando a tela
    pygame.display.flip()

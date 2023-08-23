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
player1 = pygame.Rect(0, 0, 30, 150)
player1_velocidade = 1
player1_score = 0


player2 = pygame.Rect(1250, 0, 30, 150)
player2_score = 0

ball = pygame.Rect(600, 350, 15, 15)

ball_dir_x, ball_dir_y = 1, 1

# Placar

font = pygame.font.Font(None, 50)

placar_player1 = font.render(str(player1_score), True, "white")
placar_player2 = font.render(str(player2_score), True, "white")

def redirect_ball(axis:Literal["x", "y"]):

    if axis == "x":

        ball.x = 600
        ball_dir_x *= -1

    if axis == "y":

        ball_dir_y *= -1


#loop do game
jogando = True
loop = True
while loop:

    if jogando:

        #Parte 2 - eventos
        for event in pygame.event.get():
            #evento do X de fechar
            if event.type == pygame.QUIT:
                loop = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:

                    player1_velocidade = 1

                if event.key == pygame.K_w:

                    player1_velocidade -= 1

                if event.key == pygame.K_SPACE:

                    player1.height += 50

                if event.key == pygame.K_0:

                    player2.height -= 10

        if player2_score >= 3 or player1_score >= 3:

            jogando=False


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

        #3 - parte - formas
        pygame.draw.rect(display, "white", player1)
        pygame.draw.rect(display, "white", player2)
        pygame.draw.circle(display, "white", ball.center, 8)

        display.blit(placar_player1, (500, 50))
        display.blit(placar_player2, (780, 50))

    else:

        for evento in pygame.event.get():

            if event.type == pygame.QUIT:

                loop = False

        display.fill((0, 0, 0))
        text_win = font.render("Game Over", True, "red")
        display.blit(text_win, [(640), 260])



    #atualizando a tela
    pygame.display.flip()

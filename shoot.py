import pygame
import random
pygame.font.init()


screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Shoot!")
FONT = pygame.font.SysFont("comicsans",30)
FONT2 = pygame.font.SysFont("comicsans",15)



paddle = pygame.Rect((360,520,100,20))
paddle_aim = pygame.Rect((400,490,20,30))
bullet = pygame.Rect((860,300,10,30))
enemy = pygame.Rect((0,-40,40,40))
enemy2 = pygame.Rect((0,-40,40,40))
enemy3 = pygame.Rect((0,-40,40,40))
plane = pygame.Rect((3000,250,80,20))
plane2 = pygame.Rect((-6000,300,80,20))

score = 0
loop_time = 0 
Time = 180
lose_time = 0
lose = False

run = True

rx = random.randint(0,800)
rx2 = random.randint(0,800)
rx3 = random.randint(0,800)

clock = pygame.time.Clock()

while run:
    screen.fill((217,244,241))
    clock.tick(60)

    intro_text = FONT2.render(f"Developed by Ahmed Elkallaf" , 1 , "black")
    screen.blit(intro_text,(590,560))


    if not lose:
        bullet.y -= 15
        enemy.y += 6
        enemy2.y += 6.5
        enemy3.y += 7
        enemy.x = rx
        enemy2.x = rx2
        enemy3.x = rx3
        plane.x -= 4
        plane2.x += 4

        if bullet.y <= 100:
            bullet.y = -70

        if enemy.y >= 600:
            enemy.y = -40
            rx = random.randint(0,800)

        if enemy2.y >= 600:
            enemy2.y = -40
            rx2 = random.randint(0,800)

        if enemy3.y >= 600:
            enemy3.y = -40
            rx3 = random.randint(0,800)

        if plane.x <= -1000:
            plane.x = 3000

        if plane2.x >= 1000:
            plane2.x = -6000

            
        pygame.draw.rect(screen,(0,0,255),paddle)
        pygame.draw.rect(screen,(0,0,255),paddle_aim)
        pygame.draw.rect(screen,(255,0,0),bullet)
        pygame.draw.rect(screen,(0,0,0),enemy)
        pygame.draw.rect(screen,(0,0,0),enemy2)
        pygame.draw.rect(screen,(0,0,0),enemy3)
        pygame.draw.rect(screen,(0,255,0),plane)
        pygame.draw.rect(screen,(0,255,0),plane2)

        score_text = FONT.render(f"Score: {round(score)}" , 1 , "black")
        screen.blit(score_text,(10,10))

        if loop_time >= 60:
            loop_time = 0
            Time -= 1
        else:
            loop_time += 1

        time_text = FONT.render(f"Time: {round(Time)}s" , 1 , "black")
        screen.blit(time_text,(10,50))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        key = pygame.key.get_pressed()

        if key[pygame.K_RIGHT] and paddle.x < 800 - paddle.width:
            paddle.x += 10
            paddle_aim.x += 10


        if key[pygame.K_LEFT] and paddle.x > 0:
            paddle.x -= 10
            paddle_aim.x -= 10


        if key[pygame.K_SPACE] and bullet.y <= 100 :
            bullet.y = paddle.y - 20
            bullet.x = paddle.x + 45

        if bullet.colliderect(enemy):
            bullet.y = -70
            enemy.y = -40
            rx = random.randint(0,800)
            score += 1

        if bullet.colliderect(enemy2):
            bullet.y = -70
            enemy2.y = -40
            rx2 = random.randint(0,800)
            score += 1

        if bullet.colliderect(enemy3):
            bullet.y = -70
            enemy3.y = -40
            rx3 = random.randint(0,800)
            score += 1


        if bullet.colliderect(plane):
            bullet.y = -70
            plane.x = -1000
            Time += 5

        if bullet.colliderect(plane2):
            bullet.y = -70
            plane2.x = 1000
            Time += 5


        if paddle.colliderect(enemy) or paddle.colliderect(enemy2) or paddle.colliderect(enemy3):
            Time -= 1

        
        if Time <= 0:
            lose = True

    if lose:
        lose_text = FONT.render(f"Game over" , 1 , "black")
        screen.blit(lose_text,(300,250))

        lose_time += 1
        if lose_time == 150:
            run = False

        text = FONT.render(f"Your Score is {round(score)}" , 1 , "black")
        screen.blit(text,(260,300))
        

    pygame.display.update()

pygame.quit()
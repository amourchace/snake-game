import pygame
import time
import random,os

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)
display_width = 800
display_height = 600

gameDisplay=pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game')
icon = pygame.image.load('C:/Users/sena/Desktop/images\icon.png')
pygame.display.set_icon(icon)
img = pygame.image.load('C:/Users/sena/PycharmProjects/game\head.png')
appleimg=pygame.image.load('C:/Users/sena/Desktop/images\elma1.png')

klasor = os.path.dirname(__file__)
sesKlasoru = os.path.join(klasor,"sesler")


clock = pygame.time.Clock()
block_size = 20
FPS = 15
direction = "right"
smallfont = pygame.font.SysFont('Bauhaus 93', 20)
medfont = pygame.font.SysFont('Bauhaus 93', 40)
largefont = pygame.font.SysFont('Bauhaus 93', 60)

def pause ():
    paused = True
    pygame.mixer.music.load(os.path.join(sesKlasoru, "wait.mp3"))
    pygame.mixer.music.play()
    while paused :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_SPACE:
                    pygame.mixer.music.load(os.path.join(sesKlasoru, "game1.mp3"))
                    pygame.mixer.music.play()
                    paused = False

        gameDisplay.fill(white)
        message_to_screen("Paused!", black, -100, size = "large")
        message_to_screen("Press Space to play or Escape to quit", black, 50)
        pygame.display.update()
        clock.tick(5)

def score(score):
    text = smallfont.render("Score: "+str(score), True, black)
    gameDisplay.blit(text, [0,0])

def game_intro():
    intro = True
    pygame.mixer.music.load(os.path.join(sesKlasoru, "start.mp3"))
    pygame.mixer.music.play()
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    intro = False
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()


        gameDisplay.fill(white)
        message_to_screen("Welcom to Snake Game :)", green, -100, "large")
        message_to_screen("You can eat apples!", black, -40)
        message_to_screen("You should eat more apples for the bigger!", black, 10)
        message_to_screen("Be careful! You will die!", black, 50)
        message_to_screen("Press Space to play,P to pause or Escape to quit", black, 180)

        pygame.display.update()
        clock.tick(15)



def snake(snakelist, block_size):
    if direction == "right":
        head = pygame.transform.rotate(img, 270)
    if direction == "left":
        head = pygame.transform.rotate(img, 90)
    if direction == "up":
        head = img
    if direction == "down":
        head = pygame.transform.rotate(img, 180)
    gameDisplay.blit(head, (snakelist[-1][0], snakelist[-1][1]))
    for XnY in snakelist[:-1]:

     pygame.draw.rect(gameDisplay,green, [XnY[0], XnY[1], block_size, block_size])

def text_objects(text, color, size):
    if size == "small":
     textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_to_screen(msg, color, y_displace=0, size = "small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (display_width/2), (display_height/2)+y_displace
    gameDisplay.blit(textSurf, textRect)

def gameLoop ():
    pygame.mixer.music.load(os.path.join(sesKlasoru, "game1.mp3"))
    pygame.mixer.music.play()
    global direction
    direction ='right'
    gameExit = False
    gameOver = False
    lead_x = display_width / 2
    lead_y = display_height / 2

    lead_x_change = 10
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    randAppleX = round(random.randrange(0, display_width-block_size))
    randAppleY = round(random.randrange(0, display_height-block_size))

    while not gameExit:
        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("GAME OVER!", red, -50, size = "large")
            message_to_screen("Press C to play again or Q quit", black, 50, size="medium")
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.mixer.music.pause()
                        gameExit = True
                        gameOver = False
                    elif event.key == pygame.K_c:
                        pygame.mixer.music.load(os.path.join(sesKlasoru, "game1.mp3"))
                        pygame.mixer.music.play()
                        gameLoop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_y_change = block_size
                    lead_x_change = 0
                elif event.key == pygame.K_p:
                    pause()
            if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
                pygame.mixer.music.load(os.path.join(sesKlasoru, "gameover1.mp3"))
                pygame.mixer.music.play()
                gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.fill(white)
        AppleThickness = 30
        gameDisplay.blit(appleimg, (randAppleX, randAppleY))

        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]
        for eachSegment in snakeList [:-1]:
            if eachSegment == snakeHead:
                gameOver = True


        snake(snakeList, block_size)
        score(snakeLength-1)


        pygame.display.update()
        if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness:
            if lead_y > randAppleY and lead_y < randAppleY + AppleThickness or block_size > randAppleY and lead_x + block_size < randAppleY + AppleThickness:
                randAppleX = round(random.randrange(0, display_width - block_size))
                randAppleY = round(random.randrange(0, display_height - block_size))
                snakeLength +=1
            elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:
              randAppleX = round(random.randrange(0, display_width - block_size))
              randAppleY = round(random.randrange(0, display_height - block_size))
              snakeLength +=1



        clock.tick(FPS)

    message_to_screen("You Lose!", red)
    time.sleep(2)
    pygame.display.update()
    pygame.quit()
    quit()
game_intro()
gameLoop()


# BEGIN: imports
import pygame
import random
# END: imports

# Starting pygame / Initializing pygame
pygame.init()

# BEGIN: game vars
gameWinH = 600
gameWinW = 1200
gameWinDimensions = (gameWinW, gameWinH)
gameName = "Ping X Pong"
gameIconFileName = "imgs/icon.png"
gameFontFileName = "fonts/Roboto.ttf"
gameFont = pygame.font.Font(gameFontFileName, 50)
gameRunning = True
# END: game vars

# BEGIN: window settings
screen = pygame.display.set_mode(gameWinDimensions)
pygame.display.set_caption(gameName)
winIcon = pygame.image.load(gameIconFileName).convert_alpha()
pygame.display.set_icon(winIcon)
pygame.display.set_caption(gameName, gameIconFileName)
# END: window settings

# BEGIN: Players
leftPlayerSurface = pygame.Surface((10, (gameWinH * 30) / 100))
leftPlayerRectangle = leftPlayerSurface.get_rect(midleft = (30,gameWinH/2))
leftPlayerSurface.fill((255,255,255))
leftPlayerScore = 0
leftPlayerPosition = gameWinH/2
leftPlayerScoreText = gameFont.render(f"{leftPlayerScore}", True, "White")
leftPlayerScoreRectangle = leftPlayerScoreText.get_rect(midright = (gameWinW/2 - 70, 40))

rightPlayerSurface = pygame.Surface((10, (gameWinH * 30) / 100)) 
rightPlayerSurface.fill((255,255,255))
rightPlayerRectangle = rightPlayerSurface.get_rect(midright = (gameWinW - 30,gameWinH/2))
rightPlayerScore = 0
rightPlayerPosition = gameWinH/2
rightPlayerScoreText = gameFont.render(f"{rightPlayerScore}", True, "White")
rightPlayerScoreRectangle = rightPlayerScoreText.get_rect(midleft = (gameWinW/2 + 70, 40))
# END: Players

clock = pygame.time.Clock()

# BEGIN: left area
leftSurface = pygame.Surface((gameWinW/2,gameWinH))
leftSurface.fill((6, 82, 221))
# END: left area

# BEGIN: right area
rightSurface = pygame.Surface((gameWinW/2,gameWinH))
rightSurface.fill((12, 36, 97))
# END: right area

# Ball settings
ball = pygame.Rect(gameWinW/2 - 15, gameWinH/2 - 15, 30, 30)
ballSpeedX = 15 * random.choice((1, -1))
ballSpeedY = 15 * random.choice((1, -1))

# The game loop 
while gameRunning:
    # Checking events
    for event in pygame.event.get():
        match (event.type):
            # Checking QUIT event
            case pygame.QUIT:
                gameRunning = False
            # # Getting mouse position
            # case pygame.MOUSEMOTION:
            #     leftPlayerRectangle = leftPlayerSurface.get_rect(midleft = (30,event.pos[1]))
            #     leftPlayerSurface.fill("White")
            #     break
    
    # Getting all keys
    keys = pygame.key.get_pressed()

    # Cheking if the appropriate keys are active
    if keys[pygame.K_w]:
        # Moving the left player up
        rightPlayerPosition -= 10
        leftPlayerRectangle.midleft = (30, rightPlayerPosition) 
    if keys[pygame.K_s]:
        # Moving the left player down
        rightPlayerPosition += 10
        leftPlayerRectangle.midleft = (30, rightPlayerPosition) 
    if keys[pygame.K_UP]:
        # Moving the right player up
        leftPlayerPosition -= 10
        rightPlayerRectangle.midright = (gameWinW - 30, leftPlayerPosition) 
    if keys[pygame.K_DOWN]:
        # Moving the right player down
        leftPlayerPosition += 10
        rightPlayerRectangle.midright = (gameWinW - 30, leftPlayerPosition) 

    # Rendering player areas to the screen
    screen.blit(leftSurface, (0, 0))
    screen.blit(rightSurface, (gameWinW/2, 0))

    # Rendering player score to the screen
    screen.blit(leftPlayerScoreText, leftPlayerScoreRectangle)
    screen.blit(rightPlayerScoreText, rightPlayerScoreRectangle)

    # Rendering players to the screen
    screen.blit(leftPlayerSurface, leftPlayerRectangle)
    screen.blit(rightPlayerSurface, rightPlayerRectangle)

    # Draw the ball on the screen and animate it
    pygame.draw.ellipse(screen, (255,255,255), ball)
    if ball.top <= 0 or ball.bottom >= gameWinH: ballSpeedY *= -1
    if ball.left <= 0: 
        ball.center = (gameWinW/2, gameWinH/2)
        rightPlayerScore += 1
        rightPlayerScoreText = gameFont.render(f"{rightPlayerScore}", True, "White")
    if ball.right >= gameWinW: 
        ball.center = (gameWinW/2, gameWinH/2)
        leftPlayerScore += 1
        leftPlayerScoreText = gameFont.render(f"{leftPlayerScore}", True, "White")
    if ball.colliderect(leftPlayerRectangle) or ball.colliderect(rightPlayerRectangle): ballSpeedX *= -1

    ball.x += ballSpeedX
    ball.y += ballSpeedY
    
    # Updating the screen 
    pygame.display.update()

    # Setting max framerate
    clock.tick(60)


# Quit the game
pygame.quit()

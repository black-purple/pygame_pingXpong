# BEGIN: imports
import pygame
# from sys import exit
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
leftPlayerSurface = pygame.Surface((30,(gameWinH * 30) / 100))
leftPlayerRectangle = leftPlayerSurface.get_rect(midleft = (30,gameWinH/2))
leftPlayerSurface.fill("White")
leftPlayerScore = 0

rightPlayerSurface = pygame.Surface((30,(gameWinH * 30) / 100)) 
rightPlayerSurface.fill("White")
rightPlayerRectangle = rightPlayerSurface.get_rect(midright = (gameWinW - 30,gameWinH/2))
rightPlayerScore = 0
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

leftPlayerScoreText = gameFont.render(f"Score: {leftPlayerScore}", True, "White")
rightPlayerScoreText = gameFont.render(f"Score: {rightPlayerScore}", True, "White")

# The game loop 
while gameRunning:
    # Checking events
    for event in pygame.event.get():
        match (event.type):
            # Checking QUIT event
            case pygame.QUIT:
                gameRunning = False
            # Getting mouse position
            case pygame.MOUSEMOTION:
                leftPlayerRectangle = leftPlayerSurface.get_rect(midleft = (30,event.pos[1]))
                leftPlayerSurface.fill("White")

    # Rendering player areas to the screen
    screen.blit(leftSurface, (0, 0))
    screen.blit(rightSurface, (gameWinW/2, 0))

    # Rendering player score to the screen
    screen.blit(leftPlayerScoreText, (60, 20))
    screen.blit(rightPlayerScoreText, (gameWinW - 260, 20))

    # Rendering players to the screen
    screen.blit(leftPlayerSurface, leftPlayerRectangle)
    screen.blit(rightPlayerSurface, rightPlayerRectangle)

    # 
    pygame.display.update()

    # Setting max framerate
    clock.tick(60)


# Quit the game
pygame.quit()
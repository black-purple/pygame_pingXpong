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
gameIcon = pygame.image.load(gameIconFileName)
pygame.display.set_icon(gameIcon)
pygame.display.set_caption(gameName, gameIconFileName)
# END: window settings

# BEGIN: Players
leftPlayerScore = 12
rightPlayerScore = 22
# END: Players

clock = pygame.time.Clock()

leftSurface = pygame.Surface((gameWinW/2,gameWinH))
leftSurface.fill((6, 82, 221))

rightSurface = pygame.Surface((gameWinW/2,gameWinH))
rightSurface.fill((12, 36, 97))

leftPlayerScoreText = gameFont.render(f"Score: {leftPlayerScore}", True, "White")
rightPlayerScoreText = gameFont.render(f"Score: {rightPlayerScore}", True, "White")

# The game loop 
while gameRunning:
    # Checking events
    for event in pygame.event.get():
        # Checking QUIT event
        if event.type == pygame.QUIT:
            gameRunning = False

    screen.blit(leftSurface, (0, 0))
    screen.blit(rightSurface, (gameWinW/2, 0))

    screen.blit(leftPlayerScoreText, (60, 20))
    screen.blit(rightPlayerScoreText, (gameWinW - 110, 20))
    pygame.display.update()
    clock.tick(60)


# Quit the game
pygame.quit()
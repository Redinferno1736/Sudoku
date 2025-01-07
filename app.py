# Description: This file contains the main code for the Sudoku game. It imports the required libraries and calls the functions from the functions.py file to run the game.
# The game starts by displaying the title "Sudoku" and prompting the user to choose a difficulty level (easy, medium, or hard).
# The user can select a difficulty level by clicking on the respective button.
# Importing the required libraries
import pygame
import functions

# Initialising Pygame
pygame.init()
    
# Setting screen dimensions
screen = pygame.display.set_mode((1080, 720))

# Setting game background
screen.fill("black")

# Setting the fonts of the window
font = pygame.font.SysFont("rog fonts", 64)
font1= pygame.font.SysFont("rog fonts", 32)

# Setting the title of the window
text = font.render("Sudoku", True, "white")
text_rect = text.get_rect(center=(screen.get_width() / 2, text.get_height() / 2 + 20))
screen.blit(text, text_rect)

running=True

# Difiiculty selecting loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = 1
            running = False
    
    t=font1.render("Choose Difficulty", True, "white")
    t_rect = t.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2-20))
    screen.blit(t, t_rect)

    easy_text = font1.render("Easy", True, "lightgreen")
    easy_rect = easy_text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2+60))
    screen.blit(easy_text, easy_rect)

    medium_text = font1.render("Medium", True, "darkorange")
    medium_rect = medium_text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2+110))
    screen.blit(medium_text, medium_rect)

    hard_text = font1.render("Hard", True, "firebrick")
    hard_rect = hard_text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2+160))
    screen.blit(hard_text, hard_rect)

    # Check for mouse click events
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = event.pos  # Get the mouse position

        # Check if the mouse click is within the easy button
        if easy_rect.collidepoint(mouse_pos):
            running=False
            functions.easy()
            
        # Check if the mouse click is within the medium button
        if medium_rect.collidepoint(mouse_pos):
            running=False
            functions.medium()
            
        # Check if the mouse click is within the hard button
        if hard_rect.collidepoint(mouse_pos):
            running=False
            functions.hard()
            

    # flip() the display to put your work on screen
    pygame.display.flip()

    pygame.time.delay(100)

# Exiting pygame
pygame.quit()
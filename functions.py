import pygame

# def gameboard():
#     board = [[0 for _ in range(9)] for _ in range(9)]
#     return board
    
   
def display():
    s = pygame.display.set_mode((1080, 720))
    s.fill("black")
    font1 = pygame.font.SysFont("rog fonts", 32)
    board = [[0 for _ in range(9)] for _ in range(9)]
    for i in range(10):
        if i % 3 == 0:
            pygame.draw.line(s, "wheat", (270, 120 + 60 * i), (810, 120 + 60 * i), 6)
            pygame.draw.line(s, "wheat", (270 + 60 * i, 120), (270 + 60 * i, 660), 6)
        else:
            pygame.draw.line(s, "white", (270 + 60 * i, 120), (270 + 60 * i, 660), 2)
            pygame.draw.line(s, "white", (270, 120 + 60 * i), (810, 120 + 60 * i), 2)

    running = True
    selected_cell = None

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                x, y = mouse_pos
                x, y = (x - 270) // 60, (y - 120) // 60
                if 0 <= x < 9 and 0 <= y < 9:
                    if selected_cell:
                        prev_x, prev_y = selected_cell
                        pygame.draw.rect(s, "black", (270 + 3.75 + 60 * prev_x, 120 + 3.75 + 60 * prev_y, 56, 56))
                        if board[prev_x][prev_y] != 0:
                            number = font1.render(str(board[prev_x][prev_y]), True, "white")
                            n1 = number.get_rect(center=(270 + 60 * prev_x + 30, 120 + 60 * prev_y + 30))
                            s.blit(number, n1)
                    pygame.draw.rect(s, "wheat", (270 + 3.75 + 60 * x, 120 + 3.75 + 60 * y, 56, 56))
                    selected_cell = (x, y)
                    pygame.display.update()

            if event.type == pygame.KEYDOWN and selected_cell:
                num = event.key - pygame.K_0
                if 1 <= num <= 9:
                    x, y = selected_cell
                    board[x][y] = num
                    pygame.draw.rect(s, "black", (270 + 3.75 + 60 * x, 120 + 3.75 + 60 * y, 56, 56))
                    number = font1.render(str(num), True, "white")
                    n1 = number.get_rect(center=(270 + 60 * x + 30, 120 + 60 * y + 30))
                    s.blit(number, n1)
                    selected_cell = None
                    pygame.display.update()

        pygame.display.update()

def easy():
    display()

def medium():
    display()

def hard():
    display()


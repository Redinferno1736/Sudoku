# Description: This file contains the functions that are used to fetch the Sudoku board from the API, display the board, check for user input, check if the board is solved, display the win message, display the solution, and call the API for different difficulty levels.
# The gameboard function fetches the Sudoku board from the API and returns the board and its solution.
# The display function displays the Sudoku board and checks for user input.
# The easy, medium, and hard functions call the API for different difficulty levels.
# The win function displays the win message.
# The disp_solution function displays the solution.
import pygame
import requests 
import time
import sudoku_solver as ss
import copy

# Fetch Sudoku board from API 
def gameboard(bb):
    b =bb['puzzle']
    x=[]
    c=[]
    board1=[]
    solution=[]
    for i in range(81):
        x.append(int(b[i]))
        if len(x)==9:
            board1.append(x)
            x=[]
    
    c = copy.deepcopy(board1)
    solution=ss.solve(board1)
    return c,solution
            
# Display the Sudoku board
def display(board1,solution):
    start_time = time.time()
    co=copy.deepcopy(board1)
    s = pygame.display.set_mode((1080, 720))
    s.fill("black")
    font1 = pygame.font.SysFont("rog  fonts", 32)
    clock_font = pygame.font.SysFont("rog  fonts", 24)

    for i in range(10):
        if i % 3 == 0:
            pygame.draw.line(s, "wheat", (270, 120 + 60 * i), (810, 120 + 60 * i), 6)
            pygame.draw.line(s, "wheat", (270 + 60 * i, 120), (270 + 60 * i, 660), 6)
        else:
            pygame.draw.line(s, "white", (270 + 60 * i, 120), (270 + 60 * i, 660), 2)
            pygame.draw.line(s, "white", (270, 120 + 60 * i), (810, 120 + 60 * i), 2)

    for i in range(9):
                for j in range(9):
                    num = co[i][j]
                    if num != 0:
                        text = font1.render(str(num), True, 'dodgerblue')
                        s.blit(text, (j * 60 + 286, i * 60 + 130))
    pygame.display.update()
    running = True
    selected_cell = None

    #Main game loop
    while running:
        # Calculate elapsed time
        elapsed_time = time.time() - start_time
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)
        time_text = clock_font.render(f"Time: {minutes:02}:{seconds:02}", True, "white")
        s.fill("black", (900, 10, 180, 40))
        s.blit(time_text, (900, 10))
        pygame.display.update()

        # Display the solution button
        t=font1.render("Solution", True, "greenyellow")
        sol_rect = t.get_rect(center=(120, 25))
        s.blit(t, sol_rect)

        # Check for mouse click events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Check if the mouse click is within the solution button
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if sol_rect.collidepoint(mouse_pos):
                    disp_solution(solution)
                    running = False

                x, y = mouse_pos
                x, y = (x - 270) // 60, (y - 120) // 60
                if 0 <= x < 9 and 0 <= y < 9:
                    # Clear the previous selection
                    if selected_cell:
                        prev_x, prev_y = selected_cell
                        pygame.draw.rect(s, "black", (270 + 3.75 + 60 * prev_x, 120 + 3.75 + 60 * prev_y, 56, 56))
                        if board1[prev_y][prev_x] != 0:
                            if co[prev_y][prev_x]!=0 :
                                number = font1.render(str(co[prev_y][prev_x]), True, "dodgerblue")
                            else:
                                number = font1.render(str(board1[x][y]), True, "white")
                            n1 = number.get_rect(center=(270 + 60 * prev_x + 30, 120 + 60 * prev_y + 30))
                            s.blit(number, n1)

                    pygame.draw.rect(s, "honeydew", (270 + 3.75 + 60 * x, 120 + 3.75 + 60 * y, 56, 56))
                    selected_cell = (x, y)
                    pygame.display.update()

            # Check for keyboard events
            if event.type == pygame.KEYDOWN and selected_cell:
                num = event.key - pygame.K_0
                if 1 <= num <= 9:
                    y, x = selected_cell

                    # Check if the input is valid
                    if ss.check(x, y, board1, num):
                        board1[x][y] = num
                        if board1[x][y]!= 0:
                            pygame.draw.rect(s, "black", (270 + 3.75 + 60 * y, 120 + 3.75 + 60 * x, 56, 56))
                            if co[x][y]!=0:
                                number = font1.render(str(co[x][y]), True, "dodgerblue")
                            else:
                                number = font1.render(str(board1[x][y]), True, "white")
                            n1 = number.get_rect(center=(270 + 60 * y + 30, 120 + 60 * x + 30))
                            s.blit(number, n1)
                            selected_cell = None
                        pygame.display.update()

                    # Display invalid input message
                    else:
                        inc = font1.render("Invalid Input!!!!!", True, "red")
                        in_rect = inc.get_rect(center=(s.get_width() / 2, 60))
                        s.blit(inc, in_rect)
                        pygame.display.update()
                        # Delay for 3 seconds
                        pygame.time.delay(1000)
                        
                        s.fill((0, 0, 0), in_rect)  
                        selected_cell = None
                        pygame.draw.rect(s, "black", (270 + 3.75 + 60 * y, 120 + 3.75 + 60 * x, 56, 56))

                        if board1[x][y] != 0:
                            if co[x][y]!=0:
                                number = font1.render(str(co[x][y]), True, "dodgerblue")
                            else:
                                number = font1.render(str(board1[x][y]), True, "white")
                            n1 = number.get_rect(center=(270 + 60 * y + 30, 120 + 60 * x + 30))
                            s.blit(number, n1)
                            selected_cell = None
                        pygame.display.update()

        # Check if the board is solved
        pygame.display.update()
        if all(board1[i][j] == solution[i][j] for i in range(9) for j in range(9)):
            win(elapsed_time)
            pygame.display.update()
            running = False

#Function that calls the API for easy difficulty
def easy():
    response = requests.post(
    "https://youdosudoku.com/api/",
    json={"difficulty": 'easy', "solution": True},
    headers={"Content-Type": "application/json"}
    ) 
    board = response.json()
    board1,solution=gameboard(board)
    display(board1,solution)

#Function that calls the API for medium difficulty
def medium():
    response = requests.post(
    "https://youdosudoku.com/api/",
    json={"difficulty": 'medium', "solution": True},
    headers={"Content-Type": "application/json"}
    )
    board = response.json()
    board1,solution=gameboard(board)
    display(board1,solution)

#Function that calls the API for hard difficulty
def hard():
    response = requests.post(
    "https://youdosudoku.com/api/",
    json={"difficulty": 'hard', "solution": True},
    headers={"Content-Type": "application/json"}
    )
    board = response.json()
    board1,solution=gameboard(board)
    display(board1,solution)

#Function to display the win message
def win(elapsed_time):
    sc = pygame.display.set_mode((1080, 720))
    sc.fill("black")
    font1 = pygame.font.SysFont("rog  fonts", 32)
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    text = font1.render(f"Congratulations!!!!", True, "gold")
    t=font1.render(f"you finished the puzzle in {minutes:02}:{seconds:02}", True, "white")
    a = text.get_rect(center=(sc.get_width() / 2, sc.get_height() / 2-100))
    b = t.get_rect(center=(sc.get_width() / 2, sc.get_height() / 2))
    sc.blit(text, a)
    sc.blit(t, b)
    pygame.display.update()
    pygame.time.delay(5000)

#Function to display the solution
def disp_solution(board):
    s = pygame.display.set_mode((1080, 720))
    s.fill("black")
    font1 = pygame.font.SysFont("rog  fonts", 32)
    
    for i in range(10):
        if i % 3 == 0:
            pygame.draw.line(s, "#ADD8E6", (270, 120 + 60 * i), (810, 120 + 60 * i), 6)
            pygame.draw.line(s, "#ADD8E6", (270 + 60 * i, 120), (270 + 60 * i, 660), 6)
        else:
            pygame.draw.line(s, "white", (270 + 60 * i, 120), (270 + 60 * i, 660), 2)
            pygame.draw.line(s, "white", (270, 120 + 60 * i), (810, 120 + 60 * i), 2)

    for i in range(9):
                for j in range(9):
                    num = board[i][j]
                    if num != 0:
                        text = font1.render(str(num), True, 'greenyellow')
                        s.blit(text, (j * 60 + 286, i * 60 + 130))
    pygame.display.update()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

import pygame
import requests 
import time

# Fetch Sudoku board from API 
def gameboard(board):
    b =board['puzzle']
    c=board['solution']
    x=[]
    y=[]
    board1=[]
    solution=[]
    for i in range(81):
        x.append(int(b[i]))
        y.append(int(c[i]))
        if len(x)==9 and len(y)==9:
            board1.append(x)
            solution.append(y)
            x=[]
            y=[]
    print(board1)
    print(solution)
    return board1, solution
            
def display(board1, solution):
    start_time = time.time()
    co=board1
    s = pygame.display.set_mode((1080, 720))
    s.fill("black")
    font1 = pygame.font.SysFont("rog fonts", 32)
    clock_font = pygame.font.SysFont("rog fonts", 24)

    
    for i in range(10):
        if i % 3 == 0:
            pygame.draw.line(s, "wheat", (270, 120 + 60 * i), (810, 120 + 60 * i), 6)
            pygame.draw.line(s, "wheat", (270 + 60 * i, 120), (270 + 60 * i, 660), 6)
        else:
            pygame.draw.line(s, "white", (270 + 60 * i, 120), (270 + 60 * i, 660), 2)
            pygame.draw.line(s, "white", (270, 120 + 60 * i), (810, 120 + 60 * i), 2)

    for i in range(9):
                for j in range(9):
                    num = board1[i][j]
                    if num != 0:
                        text = font1.render(str(num), True, 'wheat')
                        s.blit(text, (j * 60 + 286, i * 60 + 130))
    pygame.display.update()
    running = True
    selected_cell = None

    while running:
        elapsed_time = time.time() - start_time
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)
        time_text = clock_font.render(f"Time: {minutes:02}:{seconds:02}", True, "white")
        s.fill("black", (900, 10, 180, 40))
        s.blit(time_text, (900, 10))
        pygame.display.update()
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
                        if board1[prev_y][prev_x] != 0:
                            print("hi")
                            number = font1.render(str(board1[prev_y][prev_x]), True, "white")
                            n1 = number.get_rect(center=(270 + 60 * prev_x + 30, 120 + 60 * prev_y + 30))
                            s.blit(number, n1)
                    pygame.draw.rect(s, "#ADD8E6", (270 + 3.75 + 60 * x, 120 + 3.75 + 60 * y, 56, 56))
                    selected_cell = (x, y)
                    pygame.display.update()

            if event.type == pygame.KEYDOWN and selected_cell:
                num = event.key - pygame.K_0
                if 1 <= num <= 9:
                    y, x = selected_cell
                    print(y,x)
                    if solution[x][y] == num:
                        board1[x][y] = num
                        if board1[x][y]!= 0:
                            print("hello")
                            pygame.draw.rect(s, "black", (270 + 3.75 + 60 * y, 120 + 3.75 + 60 * x, 56, 56))
                            number = font1.render(str(num), True, "white")
                            n1 = number.get_rect(center=(270 + 60 * y + 30, 120 + 60 * x + 30))
                            s.blit(number, n1)
                            selected_cell = None
                        pygame.display.update()

                    else:
                        print("Incorrect")
                        inc = font1.render("Invalid Input!!!!!", True, "red")
                        in_rect = inc.get_rect(center=(s.get_width() / 2, 60))
                        s.blit(inc, in_rect)
                        print("hihi")
                        pygame.display.update()
                        # Delay for 3 seconds
                        pygame.time.delay(1000)
                        
                        s.fill((0, 0, 0), in_rect)  
                        selected_cell = None
                        pygame.draw.rect(s, "black", (270 + 3.75 + 60 * y, 120 + 3.75 + 60 * x, 56, 56))

                        if board1[x][y] != 0:
                            if co[x][y]!=0 and co[x][y]==board1[x][y]:
                                number = font1.render(str(board1[x][y]), True, "wheat")
                            else:
                                number = font1.render(str(board1[x][y]), True, "white")
                            n1 = number.get_rect(center=(270 + 60 * y + 30, 120 + 60 * x + 30))
                            s.blit(number, n1)
                            selected_cell = None
                        pygame.display.update()

        pygame.display.update()
        if board1 == solution:
            print("You Win")
            win(elapsed_time)
            pygame.display.update()
            running = False

def easy():
    response = requests.post(
    "https://youdosudoku.com/api/",
    json={"difficulty": 'easy', "solution": True},
    headers={"Content-Type": "application/json"}
    ) 
    board = response.json()
    board1,solution=gameboard(board)
    display(board1,solution)

def medium():
    response = requests.post(
    "https://youdosudoku.com/api/",
    json={"difficulty": 'medium', "solution": True},
    headers={"Content-Type": "application/json"}
    )
    board = response.json()
    board1,solution=gameboard(board)
    display(board1,solution)

def hard():
    response = requests.post(
    "https://youdosudoku.com/api/",
    json={"difficulty": 'hard', "solution": True},
    headers={"Content-Type": "application/json"}
    )
    board = response.json()
    board1,solution=gameboard(board)
    display(board1,solution)

def win(elapsed_time):
    s = pygame.display.set_mode((1080, 720))
    s.fill("black")
    font1 = pygame.font.SysFont("rog fonts", 32)
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    text = font1.render(f"Congratulations!!!!", True, "white")
    t=font1.render(f"you finished the puzzle in {minutes:02}:{seconds:02}", True, "white")
    a = text.get_rect(center=(s.get_width() / 2, s.get_height() / 2-100))
    b = t.get_rect(center=(s.get_width() / 2, s.get_height() / 2))
    s.blit(text, a)
    s.blit(t, b)
    pygame.display.update()
    pygame.time.delay(5000)



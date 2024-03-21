import turtle

# Setting up the screen
screen = turtle.Screen()
screen.title("Tic Tac Toe")
screen.setup(width=600, height=600)

# Drawing the board
board_pen = turtle.Turtle()
board_pen.speed(0)
board_pen.penup()
board_pen.hideturtle()
board_pen.color("black")
board_pen.pensize(5)

def draw_board():
    board_pen.penup()
    board_pen.goto(-200, 60)
    board_pen.pendown()
    board_pen.forward(400)
    board_pen.penup()
    board_pen.goto(-200, -60)
    board_pen.pendown()
    board_pen.forward(400)
    board_pen.penup()
    board_pen.goto(-60, 200)
    board_pen.setheading(-90)
    board_pen.pendown()
    board_pen.forward(400)
    board_pen.penup()
    board_pen.goto(60, 200)
    board_pen.pendown()
    board_pen.forward(400)

# Drawing X
def draw_x(row, col):
    x_pen = turtle.Turtle()
    x_pen.speed(0)
    x_pen.penup()
    x_pen.hideturtle()
    x_pen.color("blue")
    x_pen.pensize(5)
    x_pen.goto(col * 200 - 80, row * 200 - 80)
    x_pen.setheading(-45)
    x_pen.pendown()
    for _ in range(4):
        x_pen.forward(113)
        x_pen.backward(113)
        x_pen.left(90)

# Drawing O
def draw_o(row, col):
    o_pen = turtle.Turtle()
    o_pen.speed(0)
    o_pen.penup()
    o_pen.hideturtle()
    o_pen.color("red")
    o_pen.pensize(5)
    o_pen.goto(col * 200, row * 200 - 160)
    o_pen.setheading(0)
    o_pen.pendown()
    o_pen.circle(80)

# Game logic
board = [[' ' for _ in range(3)] for _ in range(3)]
turn = 'X'

def check_winner():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None

def click(x, y):
    global turn
    row = int((y + 300) // 200)
    col = int((x + 300) // 200)
    if board[row][col] == ' ':
        if turn == 'X':
            draw_x(row, col)
            board[row][col] = 'X'
            turn = 'O'
        else:
            draw_o(row, col)
            board[row][col] = 'O'
            turn = 'X'
        winner = check_winner()
        if winner:
            turtle.penup()
            turtle.goto(-100, 0)
            turtle.write(f"{winner} wins!", align="center", font=("Arial", 48, "normal"))

# Setting up the game
draw_board()
screen.onclick(click)

# Run the game
turtle.done()
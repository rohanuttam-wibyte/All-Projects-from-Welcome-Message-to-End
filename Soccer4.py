import turtle
import random

screen = turtle.Screen()
screen.setup(800,700)
screen.setworldcoordinates(-500,-500,500,500)
screen.title("Soccer Connect 4 - Match Day!")
turtle.speed(0)
turtle.hideturtle()
screen.tracer(0,0) 
t = turtle.Turtle()
t.up()

writer = turtle.Turtle()
writer.hideturtle()
writer.up()

def draw_rectangle():
  t.goto(-350, -100)
  t.fillcolor('forestgreen')
  t.pendown()
  t.begin_fill()
  t.goto(-350, 500)
  t.goto(350, 500)
  t.goto(350, -100)
  t.goto(-350, -100)
  t.end_fill()
  t.up()
  
  t.goto(-350, -100)
  t.pencolor('white')
  t.pensize(4)
  t.pendown()
  t.goto(-350, 500)
  t.goto(350, 500)
  t.goto(350, -100)
  t.goto(-350, -100)
  t.up()
  t.pencolor('black') 
  t.pensize(1)

Nrows = 6
Ncols = 7

def draw_circle(x, y, r, fillcolor):
  t.goto(x, y)
  t.setheading(-90)
  t.fillcolor(fillcolor)
  t.begin_fill()
  t.circle(r)
  t.end_fill()

board = [[0 for i in range(Ncols)] for j in range(Nrows)]

def draw_board():
  draw_rectangle()

  for kk in range(Nrows):
    for jj in range(Ncols):
      if board[kk][jj] == 0:
        draw_circle(-340 + jj*100, 450 - kk*100, 40, 'white') 
      if board[kk][jj] == 1:
        draw_circle(-340 + jj*100, 450 - kk*100, 40, 'red') 
      if board[kk][jj] == 2:
        draw_circle(-340 + jj*100, 450 - kk*100, 40, 'blue') 

def all_same(cells, value):
  allequal = True
  for cell in cells: 
    if cell != value:
      allequal = False
      break
  return allequal
  
def checkHorizontalWinner(value):
  winner = False
  for jj in range(Nrows):
    for kk in range(4):
      cells = []
      for cnt in range(4):
        cells.append(board[jj][kk+cnt])
      if all_same(cells, value):
        winner = True
        break
  return winner

def checkVerticalWinner(value):
  winner = False
  for jj in range(3):
    for kk in range(Ncols):
      cells = []
      for cnt in range(4):
        cells.append(board[jj+cnt][kk])
      if all_same(cells, value):
        winner = True
        break
  return winner

def checkDiagonalOneWinner(value):
  winner = False
  for jj in range(3,Nrows,1):
    for kk in range(4):
      cells = []
      for cnt in range(4):
        cells.append(board[jj-cnt][kk+cnt])
      if all_same(cells, value):
        winner = True
        break
  return winner

def checkDiagonalTwoWinner(value):
  winner = False
  for jj in range(0,3,1):
    for kk in range(4):
      cells = []
      for cnt in range(4):
        cells.append(board[jj+cnt][kk+cnt])
      if all_same(cells, value):
        winner = True
        break
  return winner

def checkwinner(value):
  winner = checkHorizontalWinner(value)
  if not winner:
    winner = checkVerticalWinner(value)
    if not winner:
      winner = checkDiagonalOneWinner(value)
      if not winner:
        winner = checkDiagonalTwoWinner(value)
  return winner

def lowest_row(col):
  r = -1
  for kk in range(Nrows-1, -1, -1):
    if board[kk][col] == 0:
      r = kk
      break
  return r

def announce_winner(msg):
  writer.goto(0, -180)
  writer.color("black")
  writer.write(msg, align="center", font=("Arial", 28, "bold"))

def play(x, y):
  global turn, gameOver
  if gameOver:
    return
  
  col = int((x + 350)//100)
  
  if col < 0: 
    col = 0
  if col > Ncols-1:
    col = Ncols - 1

  avail_cols = find_open_cols()

  if col in avail_cols:
    available_row = lowest_row(col)
    board[available_row][col] = 1
  
    draw_board()
    if checkwinner(1):
      gameOver = True
      announce_winner('GOOOOOAL! Home Team (Red) Wins! 🏆')
    else:
      turn = 2
  
  if turn == 2:
    playc()
  
def find_open_cols():
  open_cols = [m for m in range(Ncols)]
  full_cols = []

  for col in open_cols:
    if lowest_row(col) == -1:
      full_cols.append(col)

  for col in full_cols:
    open_cols.remove(col)

  return open_cols

def display_board():
  for kk in range(Nrows):
    print(board[kk])

def get_best_move():
  avail_cols = find_open_cols()
  
  for col in avail_cols:
    row = lowest_row(col)
    board[row][col] = 2
    if checkwinner(2):
      board[row][col] = 0
      return col
    board[row][col] = 0

  for col in avail_cols:
    row = lowest_row(col)
    board[row][col] = 1
    if checkwinner(1):
      board[row][col] = 0
      return col
    board[row][col] = 0

  if 3 in avail_cols:
    return 3

  return random.choice(avail_cols)

def playc():
  global turn, gameOver
  cols_avail = find_open_cols()
  
  if len(cols_avail) > 0:
    col = get_best_move()
    available_row = lowest_row(col)
    board[available_row][col] = 2  
  
  draw_board()
  if checkwinner(2):
    gameOver = True
    announce_winner('GOOOOOAL! Away Team (Blue) Wins! 🏆')
  else:
    turn = 1

gameOver = False   
turn = 1

draw_board()
screen.onclick(play)
turtle.done()

import pygame
import random

from constants import BLACK, ROWS, RED, SQUARE_SIZE, COLS, WHITE, YELLOW, GREY
from piece import Piece

class Board:

  ##################################################################
    
    # Functions for initializing the board.

  def __init__(self):
    self.board = []
    self.create_board()
    
    # Creates the board. Each "Piece" is set equal to 0.
  def create_board(self):
    for row in range(ROWS):
      self.board.append([])
      for col in range(COLS):
        self.board[row].append(0)

  ##################################################################

  # Functions for drawing the board.

  # this function is called by draw(). It will draw the grey circles on the board.
  def draw_circles(self, win):
        
    for row in range(ROWS):
      for col in range(COLS):
        x = SQUARE_SIZE * col + SQUARE_SIZE // 2
        y = SQUARE_SIZE * row + SQUARE_SIZE // 2
        radius = SQUARE_SIZE//2
        pygame.draw.circle(win, BLACK, (x, y), radius - 2)
        pygame.draw.circle(win, GREY, (x, y), radius - 4)

    # draws the board
  def draw(self, win):
    win.fill(YELLOW)
    self.draw_circles(win)
    for row in range(ROWS):
      for col in range(COLS):
        piece = self.board[row][col]
        if piece != 0:
          piece.draw(win)

  # prints the board to the console.
  def print(self):
    for row in range(ROWS):
      for column in range(COLS):
        if self.board[row][column] == 0:
          print("_ ", end='')
        elif self.board[row][column].color == RED:
          print("r ", end='')
        else:
          print("w ", end='')
      print()
    print()


  ##################################################################
  # Functions for adding Pieces to the board and finding empty spots.

  # Given a column, add_piece will "drop" the piece to the lowest open row. The function returns False if the column is full.
  def add_piece(self, color, column):
    for row in reversed(range(ROWS)):
      if self.board[row][column] == 0:
        self.board[row][column] = Piece(row, column, color)
        return True
      
    return False

  # return the Piece at [row][column]
  def get_piece(self, row, column):
    return self.board[row][column]


  # returns the index of the top piece in column.
  def get_top_piece(self,column):
    for row in reversed(range(ROWS)):
      if self.board[row][column] == 0:
        return row + 1 if row < ROWS - 1 else ROWS - 1
      
    return 0

  # returns the index of the first empty spot in column or -1 if the column is full.
  def get_first_empty_spot(self,column):
    for row in reversed(range(ROWS)):
      if self.board[row][column] == 0:
        return row
      
    return -1

  # returns a list with the index of the first empty spot in each column and -1 if a column is full.
  def get_valid_moves(self):
    moves = []

    for column in range(COLS):
      moves.append(self.get_first_empty_spot(column))

    return moves

  def is_full(self):
    for row in range(ROWS):
      for col in range(COLS):
        if self.board[row][col] == 0:
          return False

    print("tie")
    return True

  ##################################################################
    
    # Functions for checking to see if there is a winner.

    # this function checks to see if color has won the game.
    # return true if there is, false if there isn't.
  def winner(self, color):
    return self.diagonal_winner(color) or self.vertical_winner(color) or self.horizontal_winner(color) 

    # checks to see if color has won the game by getting four in a row vertically.
  def vertical_winner(self, color):
    counter = 0
    for column in range(COLS):
      for row in range(ROWS):
        if self.board[row][column] != 0 and self.board[row][column].color == color:
          counter += 1
        else:
          counter = 0

        if counter == 4:
          return True

      counter = 0

    return False

    # checks to see if color has won the game by getting four in a row horizontally.
  def horizontal_winner(self, color):
    counter = 0
    for row in range(ROWS):
      for column in range(COLS):
        if self.board[row][column] != 0 and self.board[row][column].color == color:
          counter += 1
        else:
          counter = 0

        if counter == 4:
          return True

      counter = 0
        
    return False

    # checks to see if color has won the game by getting four in a row diagonally. This code seems way more complicated than it needs to be.
  def diagonal_winner(self, color):

    counter = 0
    
    #diagonal down
    for row in range(3):
      for column in range(4):
        while counter < 4 and self.board[row + counter][column + counter] != 0 and self.board[row + counter][column + counter].color == color:
          counter += 1

        if counter == 4:
          return True
        counter = 0

      counter = 0

    #diagonal up
    for row in range(3):
      for column in range(4):
        while counter < 4 and self.board[row + counter][6 - column - counter] != 0 and self.board[row + counter][6 - column - counter].color == color:
          counter += 1

        if counter == 4:
          return True
        counter = 0
      
      counter = 0
      
    return False

  ##################################################################
  # Functions for drawing winning lines

  # Returns a list of tuples for every winning window.
  # Each tuple contains the pixel coordinates of the first and last piece in the window.
  def get_winning_windows(self, color):
    winning_windows = []
    # Horizontal wins.
    for row in range(ROWS):
      for col in range(COLS - 3):
        if (self.board[row][col] != 0 and self.board[row][col].color == color and
                self.board[row][col + 1] != 0 and self.board[row][col + 1].color == color and
                self.board[row][col + 2] != 0 and self.board[row][col + 2].color == color and
                self.board[row][col + 3] != 0 and self.board[row][col + 3].color == color):
          start = (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2)
          end = ((col + 3) * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2)
          winning_windows.append((start, end))

    # Vertical wins.
    for col in range(COLS):
      for row in range(ROWS - 3):
        if (self.board[row][col] != 0 and self.board[row][col].color == color and
                self.board[row + 1][col] != 0 and self.board[row + 1][col].color == color and
                self.board[row + 2][col] != 0 and self.board[row + 2][col].color == color and
                self.board[row + 3][col] != 0 and self.board[row + 3][col].color == color):
          start = (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2)
          end = (col * SQUARE_SIZE + SQUARE_SIZE // 2, (row + 3) * SQUARE_SIZE + SQUARE_SIZE // 2)
          winning_windows.append((start, end))

    # Diagonal down-right wins.
    for row in range(ROWS - 3):
      for col in range(COLS - 3):
        if (self.board[row][col] != 0 and self.board[row][col].color == color and
                self.board[row + 1][col + 1] != 0 and self.board[row + 1][col + 1].color == color and
                self.board[row + 2][col + 2] != 0 and self.board[row + 2][col + 2].color == color and
                self.board[row + 3][col + 3] != 0 and self.board[row + 3][col + 3].color == color):
          start = (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2)
          end = ((col + 3) * SQUARE_SIZE + SQUARE_SIZE // 2, (row + 3) * SQUARE_SIZE + SQUARE_SIZE // 2)
          winning_windows.append((start, end))

    # Diagonal up-right wins.
    for row in range(3, ROWS):
      for col in range(COLS - 3):
        if (self.board[row][col] != 0 and self.board[row][col].color == color and
                self.board[row - 1][col + 1] != 0 and self.board[row - 1][col + 1].color == color and
                self.board[row - 2][col + 2] != 0 and self.board[row - 2][col + 2].color == color and
                self.board[row - 3][col + 3] != 0 and self.board[row - 3][col + 3].color == color):
          start = (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2)
          end = ((col + 3) * SQUARE_SIZE + SQUARE_SIZE // 2, (row - 3) * SQUARE_SIZE + SQUARE_SIZE // 2)
          winning_windows.append((start, end))

    return winning_windows

  # Draws a line across each winning window found for the specified color.
  def draw_win_lines(self, win, color):
    # You can change the color of the win line if desired; here we use green.
    win_line_color = (0, 255, 0)
    for start, end in self.get_winning_windows(color):
      pygame.draw.line(win, win_line_color, start, end, 5)

# Muhammad Wajahat Mirza (mwm356) 
# Intro to Computer Science 
# Game Minesweeper Code
# Python in Processing
# Two classes: Cell and board 
# Random assignment of 10 mines
# Assign digit numbers to the no. of mines present next to empty cells
# Add recursive code to check if adjacent cells are empty 
# Show win game or game over 

import os
from random import choice

path=os.getcwd()   # this is the directory 


num_rows    = 10   # dimensions of rows can easily be changed by altering this global variable
num_cols    = 10   # dimensions of columns can easily be changed by altering this global variable
num_mines   = 10   # num of mines to be present on the board. It can easily be changed
cell_height = 64   # this is the height of the screen that can be changed if need be
cell_width  = 64   # this is the width of the screen that can be changed if need be

gui_img = ["0","1","2","3","4","5","6","7","8","gameover","mine","tile","win"]    # make a list of all the images to be used in displaying the board


class Cell: 
    def __init__(self, row, col, status = "unexplored"):
        self.row     = row 
        self.col     = col 
        self.gui_img = "0"            # this sets the background of the board. Here it would be grey silver color empty tile 
        self.status  = "unexplored"   # this is the initial status of the cell board i.e. unexplored 

        self.img_num = loadImage(path + "/images/tile.png")                  # this will lead to grey silver color img display 
    
    def display(self): 
        if self.status == "unexplored":  
            image(self.img_num, self.col * cell_width, self.row * cell_height)   # if tile is unexplored, it should show silver lined tile
        elif self.status == "explored": 
            self.img = loadImage(path + "/images/" + self.gui_img + ".png")
            image(self.img, self.col * cell_width, self.row * cell_height)       # if tile is explored, it should show whether it is empty, mine, or a digit 

class Board: 
    def __init__(self):
        self.num_rows   = num_rows
        self.num_cols   = num_cols 
        self.num_mines  = num_mines
        self.tiles_left = self.num_rows * self.num_cols - self.num_mines           # this will give the number of tiles without 10 mines
        
        self.game_over  = False                                                    # this is the initial status of the game
        self.game_over_img  = loadImage(path + "/images/" + gui_img[9]  + ".png")  # this will show the game over image if mine is hit
        self.game_won_img   = loadImage(path + "/images/" + gui_img[12] + ".png")  # this will show game won if all tiles are targeted without hitting mines
        
        self.board = [] 
        for row in range(self.num_rows): 
            for col in range(self.num_cols): 
                self.board.append(Cell(row, col))     # Board will collect coordinates for all cells/tiles    
        self.allocate_mines()     # this method will randomly assign mines
        self.allocate_digits()    # this method will calculate how far are mines from the explored tile
        
    def allocate_mines(self):     # Randomly assigning mines 
        for mine in range(self.num_mines): 
            placed = choice(self.board)     
            while placed.gui_img == "mine":
                placed = choice(self.board)
            placed.gui_img = "mine" # Giving mine image to the randomly assigned cells
            
    def allocate_digits(self):
        for placed in self.board:
            if placed.gui_img != "mine":
                for numRow in [placed.row - 1, placed.row, placed.row + 1]:         # this algorithm will check the neighboring empty cells and place images respectively
                    for numCol in [placed.col - 1, placed.col, placed.col + 1]:
                        numPlaced = self.obtain_cell(numRow, numCol)
                        if numPlaced != None and numPlaced.gui_img == "mine":
                            placed.gui_img = str(int(placed.gui_img) + 1) 
                placed.img = loadImage(path + "/images/" + placed.gui_img + ".png") 
    
    def obtain_cell(self, row, col):             
        for seq in self.board:
            if seq.row == row and seq.col == col:
                return seq
            
    def display_board(self):                   # this method will display the result. Change the size of the image if need be
        for tie in self.board: 
            tie.display() 
        if self.game_over: 
            image(self.game_over_img, 25, 25)
        if self.tiles_left == 0:
            image(self.game_won_img, 25, 25)
            
    def explore_cell(self, placed):            # this method will check the explored cell, and update the status of the game
        if placed.gui_img == "mine":
            for placed in self.board:
                placed.status = "explored"
            self.game_over = True 
            return
        
        if placed.gui_img != "0":
            placed.status = "explored"
            self.tiles_left -= 1
            if self.tiles_left == 0: 
                self.game_won_img
            return
        
        placed.status = "explored"
        self.tiles_left -= 1
        for numRow in [placed.row - 1, placed.row, placed.row + 1]:
            for numCol in [placed.col - 1, placed.col, placed.col + 1]:
                numPlaced = self.obtain_cell(numRow, numCol) 
                if numPlaced != None and numPlaced.status == "unexplored":
                    self.explore_cell(numPlaced)          # recursive function 
 
board = Board()

def setup():       #set up function
    board = Board() 
    size(num_rows * cell_height, num_cols * cell_height)
    background(180)
    
def draw():        # draw and display 
    background(180)
    board.display_board()
            
def mouseClicked(self):      # this gives back where tile user clicked 
    col = mouseX // cell_width
    row = mouseY // cell_height
    explored_cell = board.obtain_cell(row, col)
    board.explore_cell(explored_cell)        # explore_cell and explored_cell are two different variables
    
    print("Clicked at " + str(row) + ", " + str(col))    # to show coordinates of the tile
    location = ((col) + (row*num_cols))
    print(location)                          # which cell number was clicked 
    #board.board[location].display()

# End of code

import pygame # imports the pygame library
import math # imports the math library
import random # imports the random library
import sys # imports sys 

# this class will allow each cell to have its own properties that can be modified
class Cell:
    
    # this is just the initialization function
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.neighbors = []
        self.previous_node = None
        self.wall = False
        self.f_score = float(0)
        self.g_score = float(0)
        self.h_score = float(0)

    # this function adds all the neighbors for each cell
    def addNeighbors(self, grid, column, row, count_diagonal):
        if self.x_pos > 0:
            self.neighbors.append(grid[self.x_pos - 1][self.y_pos])
        if self.x_pos < column - 1:
            self.neighbors.append(grid[self.x_pos + 1][self.y_pos])
        if self.y_pos > 0:
            self.neighbors.append(grid[self.x_pos][self.y_pos - 1])
        if self.y_pos < row - 1:
            self.neighbors.append(grid[self.x_pos][self.y_pos + 1])       
        
        # this extra feature will add all the diagonals as neighbors
        if count_diagonal == True:
            if self.x_pos > 0 and self.y_pos < row - 1:
                self.neighbors.append(grid[self.x_pos - 1][self.y_pos + 1])
            if self.x_pos > 0 and self.y_pos > 0:
                self.neighbors.append(grid[self.x_pos - 1][self.y_pos - 1])
            if self.x_pos < column - 1 and self.y_pos < row - 1:
                self.neighbors.append(grid[self.x_pos + 1][self.y_pos + 1])
            if self.x_pos < column - 1 and self.y_pos > 0:
                self.neighbors.append(grid[self.x_pos + 1][self.y_pos - 1])

    # this function will set the color of the cell
    def colorCell(self, win, color, shape):
        side = 20
        if shape == "node":
            pygame.draw.circle(win, color, (self.x_pos*side+9, self.y_pos*side+9), side//3)
        elif shape == "small square":
            pygame.draw.rect(win, color, (self.x_pos * side, self.y_pos * side, side - 2, side - 2))
        elif shape == "circle":
            pygame.draw.circle(win, color, (self.x_pos*side+9, self.y_pos*side+9), side//6)

class Visualizer:
    
    # this function displays the screen when there is no solution
    def displayResultScreen(self):
        self.displayImage(pygame.image.load('./images/no_solution.png')) # passes the image to displayImage function
        pygame.display.flip() # updates the pygame application
        pygame.time.wait(3000) # waits for 3 seconds before continuing the program

    # this function will check if the user wants to quit the program
    def checkForExit(self):
        for event in pygame.event.get(): # gets the user input
            if event.type == pygame.QUIT: # checks if the event type is quit
                self.exitProgram() # calls the exit program function

    # this function exits the pygame screen and ends the program
    def exitProgram(self):
        self.displayImage(pygame.image.load('./images/exit_screen.jpg')) # displays the goodbye screen
        pygame.display.flip() # updates the pygame display
        pygame.time.wait(1500) # shows the screen for 1.5 seconds
        pygame.quit() # quits the application
        sys.exit() # exits the program

    # this function will determine what cell the mouse is hovering over and then change the state of the cell
    def selectWall(self, mouse_pos, new_state, end_node, start_node): # takes 4 variables as parameters
        x = mouse_pos[0] // 20 # determines the x index
        y = mouse_pos[1] // 20 # determines the y index
        if grid[x][y] != end_node and grid[x][y] != start_node: # ensures the current cell is not the start or end node
            grid[x][y].wall = new_state # changes the state of the cell

    # this function will determine what cell the mouse is hovering over and then return the value
    def selectStart(self, mouse_pos, start_node, end_node):
        x = mouse_pos[0] // 20 # determines the x index
        y = mouse_pos[1] // 20 # determines the y index
        # print(str(x) + " " + str(y)) # this print statement can be uncommented to see the x and y of the start cell
        if grid[x][y] != end_node: # ensures the cell is not the end node
            return grid[x][y] # returns the corresponding cell
        else:
            return start_node # returns the original start node

    # this function will determine what cell the mouse is hovering over and then return the value
    def selectEnd(self, mouse_pos, start_node , end_node): 
        x = mouse_pos[0] // 20 # determines the x index
        y = mouse_pos[1] // 20 # determines the y index
        if grid[x][y] != start_node: # ensures the cell is not the start node
            return grid[x][y] # returns the corresponding cell
        else:
            return end_node # returns the original end node

    # this is the heurisitic function that the A* algorithm uses
    def heuristic(self, current_node, end_node):
        # returns the absolute euclidean distance between the current and end node
        return math.sqrt((current_node.x_pos - end_node.x_pos)**2 + abs(current_node.y_pos - end_node.y_pos)**2)  

    # this function will draw the grid and color each cell with the correct color
    def drawGrid(self):
        screen.fill((127, 195, 180)) # fills the entire screen with a light green which will later be the color of the grid lines
        
        # this loop will cycle through all the cells in the grid
        for y in range(grid_rows): 
            for x in range(grid_col):
                
                cell = grid[x][y] 
                cell.colorCell(screen, (244,250,250), "small square") # this is the color of a regular cell
                if cell == start: # checks if the cell is the start node
                    cell.colorCell(screen, (0, 153, 0), "node")
                
                elif cell == end: # checks if the cell is the end node
                    cell.colorCell(screen, (204, 0, 0), "node")
                
                elif cell in path: # checks if the cell is in the path list
                    cell.colorCell(screen, (24, 90, 90), "small square")
                
                elif cell in open_set: # checks if the cell is in the open_set list
                    cell.colorCell(screen, (255, 153, 51), "circle")
                
                elif cell in closed_set: # checks if the cell is in the closed_set list
                    cell.colorCell(screen, (255, 153, 51), "small square")
                
                elif cell.wall: # checks if the cell is a wall
                    cell.colorCell(screen, (2, 18, 30), "small square")
                    
        pygame.display.update() # updates the pygame display to show the new changes

    # this function will backtrack to determine all the cells that are in the shortest path
    def aStarBackTrack(self, current): # takes the current node as the only parameter
        # print("Backtracking called.") # this print statement is used for debugging
        in_path = current # assigns the current to the path_node
        while in_path.previous_node != None: # runs the loop until it reaches the start node
            self.checkForExit() 
            path.append(in_path.previous_node) # adds the previous node to the path list
            in_path = in_path.previous_node # assigns the previouse node to the in_path variable
            self.drawGrid()
        # print("Done Backtracking") # this print statement should be uncommented when debugging the program

    def aStarSearch(self):

        start.h_score = self.heuristic(start, end) # determines the absolute euclidean distance from the start node to end node
        open_set.append(start) # adds the start node to the open_set list   
        while len(open_set) > 0:
            
            self.checkForExit()
            
            lowest_f_score_index = 0
            for index in range(len(open_set)):
                if open_set[index].f_score < open_set[lowest_f_score_index].f_score:
                    lowest_f_score_index = index

            current_node = open_set[lowest_f_score_index]
            
            
            if current_node == end:
                open_set.remove(current_node)
                self.aStarBackTrack(current_node)
                return

            open_set.remove(current_node)
            closed_set.append(current_node)

            for neighbor in current_node.neighbors:
                
                if neighbor in closed_set or neighbor.wall:
                    continue
                
                new_g_score = current_node.g_score + 1
                use_new_path = False
                
                if neighbor in open_set:
                    if new_g_score < neighbor.g_score:
                        neighbor.g_score = new_g_score
                        use_new_path = True
                
                else:
                    neighbor.g_score = new_g_score
                    use_new_path = True
                    open_set.append(neighbor)
                
                if use_new_path == True:
                    neighbor.h_score = self.heuristic(neighbor, end)
                    neighbor.f_score = neighbor.g_score + neighbor.h_score
                    neighbor.previous_node = current_node
            
            self.drawGrid()
        self.displayResultScreen()
        
    def displayImage(self, image):    
        screen.blit(image, (0,0))
        pygame.display.flip()

    def displayPages(self):
        tutorial_images = [pygame.image.load('./images/screen_1.jpg'), pygame.image.load('./images/screen_2.jpg'), pygame.image.load('./images/screen_3.png'), pygame.image.load('./images/screen_4.jpg'), 
        pygame.image.load('./images/screen_5.jpg'), pygame.image.load('./images/screen_6.jpg'), pygame.image.load('./images/screen_7.png')]
        tutorial_index = 0

        while tutorial_index < len(tutorial_images):
            self.displayImage(tutorial_images[tutorial_index])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exitProgram()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        tutorial_index += 1
                    if event.key == pygame.K_LEFT:
                        if tutorial_index != 0:
                            tutorial_index-= 1

    def clearWall(self):
        for x in range(grid_col):
            for y in range(grid_rows):
                grid[x][y].wall = False

    def generateRandomWalls(self):

        self.clearWall()

        for x in range(grid_col-1):
            for y in range(grid_rows-1):
                if grid[x][y] == start or grid[x][y] == end:
                    continue
                else:
                    if random.randint(1, 1000) < 224:
                        grid[x][y].wall = True                    
                    else:
                        continue
            self.drawGrid()

    # this function will initialize the grid that will be used for the logic of the program
    def initGrid(self):
        # adds all the cells to the grid
        for x in range(grid_col): # loops through every column
            row_list = [] # instantiates a new list
            for y in range(grid_rows): # loops through every row
                row_list.append(Cell(x, y)) # adds a cell for each row
            grid.append(row_list) # adds the row_list to the grid list
        
        # adds the neighbors of all the cells in the grid
        for x in range(grid_col):
            for y in range(grid_rows):
                grid[x][y].addNeighbors(grid, grid_col, grid_rows, use_diagonal)
                grid[x][y].wall = False
        
# initializes constant variables
grid = []
grid_rows = 40
grid_col = 60
side_length = 20
screen_length = grid_col * side_length
screen_width = grid_rows * side_length
use_diagonal = True
screen_size = (screen_length, screen_width)

# initializes the pygame application
pygame.init() 
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Pathfinding Visualizer")

vis = Visualizer()
# displays the tutorial pages
vis.displayPages()

# main program loop
while True:

    vis.initGrid()
    start = grid[5][18]
    end = grid[54][18]

    # instantiates/resets all the lists
    open_set = []
    closed_set = []
    path = []

    # initializes all the flag variables
    is_selecting_start = True
    is_selecting_end = False
    is_selecting_walls = False 
    start_search = False
    reset_game = False

    vis.drawGrid() # draws the current grid
    pygame.display.flip() 

    while True:
        
        if is_selecting_start == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    vis.exitProgram()
                if event.type == pygame.MOUSEBUTTONDOWN:  
                    if event.button in (1, 3): 
                        start = vis.selectStart(pygame.mouse.get_pos(), start, end)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        is_selecting_start = False
                        is_selecting_end = True
                    if event.key == pygame.K_c:
                        reset_game = True
        
        if is_selecting_end == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    vis.exitProgram()
                if event.type == pygame.MOUSEBUTTONDOWN:  
                    if event.button in (1, 3): 
                        end = vis.selectEnd(pygame.mouse.get_pos(), start, end)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        is_selecting_end = False
                        is_selecting_walls = True
                    if event.key == pygame.K_c:
                        reset_game = True

        if is_selecting_walls == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    vis.exitProgram()
                if event.type == pygame.MOUSEBUTTONDOWN:  
                    if event.button in (1, 3): 
                        vis.selectWall(pygame.mouse.get_pos(), event.button==1, end, start)
                if event.type == pygame.MOUSEMOTION:
                    if event.buttons[0] or event.buttons[2]:  
                        vis.selectWall(pygame.mouse.get_pos(), event.buttons[0], end, start) 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        start_search = True
                        is_selecting_walls = False
                    if event.key == pygame.K_c:
                        reset_game = True
                    if event.key == pygame.K_w:
                        vis.generateRandomWalls()
                    if event.key == pygame.K_BACKSPACE:
                        vis.clearWall()

        if start_search == True:
            vis.aStarSearch()
            vis.drawGrid()
            start_search = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                vis.exitProgram()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    reset_game = True
        
        if reset_game == True:
            break

        vis.drawGrid()
        pygame.display.flip()
            

            
    
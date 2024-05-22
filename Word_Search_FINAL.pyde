import random

def mouseReleased():
    global game_state, active_buttons, active_square_buttons
    global current_button_pressed, current_coordinate_pressed
    #Take in mousex and mousey
    #Check the game_state
    #Take in the buttons in the game_state
    #Return the button as button_pressed and set to None when nothing is pressed
    if game_state == "start_menu":
        active_buttons_keys = active_buttons.keys()
    
        for i in range(len(active_buttons_keys)): #Go through every single active button boundary and check if the mouse x and y are in that bound, if true then set current_bound_pressed as that button name
            if mouseX > active_buttons[active_buttons_keys[i]][1] and mouseX < active_buttons[active_buttons_keys[i]][3]:
                if mouseY > active_buttons[active_buttons_keys[i]][2] and mouseY < active_buttons[active_buttons_keys[i]][4]:
                    current_button_pressed = active_buttons[active_buttons_keys[i]][0]
            else:
                current_button_pressed = None
    
    if game_state == "easy_map" or game_state == "medium_map" or game_state == "hard_map":
        
        number_of_rows = len(active_square_buttons)
        number_of_cols = len(active_square_buttons[0])

        for i in range(number_of_rows): #i is the y value
            for j in range(number_of_cols): #j is the x value
                if mouseX > active_square_buttons[i][j][0] and mouseX < active_square_buttons[i][j][2]:
                    if mouseY > active_square_buttons[i][j][1] and mouseY < active_square_buttons[i][j][3]:
                        
                        if current_coordinate_pressed[0] == None:
                            current_coordinate_pressed[0] = [j, i]
                            clickOneDrawer()
                            print(current_coordinate_pressed)
                            print(answer_bank)
                        elif current_coordinate_pressed[1] == None:
                            current_coordinate_pressed[1] = [j, i]
                            clickTwoDrawer()
                            print(current_coordinate_pressed)
                            print(answer_bank)
                        else:
                            current_coordinate_pressed[0] = [j, i]
                            current_coordinate_pressed[1] = None
                            clickOneDrawer()
                            print(current_coordinate_pressed)
                            print(answer_bank)

def clickOneDrawer():
    rectMode(CORNERS)
    textAlign(CORNER)
    fill(200)
    noStroke()
    rect(0, 725, 90, 750)
    fill(0)
    text("Click ONE", 10, 740)
    
def clickTwoDrawer():
    rectMode(CORNERS)
    textAlign(CORNER)
    fill(200)
    noStroke()
    rect(0, 725, 90, 750)
    fill(0)
    text("Click TWO", 10, 740)

def currentCoordinateChecker(current_coords):
    #Takes in an arr that has 2 tuples such that the first tuple is the first square pressed and
    #and the second tuple is the second square pressed. ex. [(2, 5), (2, 1)]
    if current_coords[1] != None:
        if answerChecker(current_coords) == True:
            return True

def answerChecker(current_coords): #Returns true of the select coords are in the answer bank
    global answer_bank
    if current_coords in answer_bank:
        answer_bank.remove(current_coords)
        return True

def startMenu():
    global active_buttons, window_info, current_button_pressed
    global game_state, current_level_name
    
    #Parse information from dict to usable variables
    
    start_buttons = {
        "easy" : ["Easy Map", (window_info["width"] / 2) , 150, 200, 100],
        "medium" : ["Medium Map", (window_info["width"] / 2), 350, 200, 100],
        "hard" : ["Hard Map", (window_info["width"] / 2), 550, 200, 100] 
        #[button name, x, y, widthx, heighty]
        }
    
    dictkeys = start_buttons.keys()
    
    for i in range(len(dictkeys)):
        button_name = start_buttons[dictkeys[i]][0] #Get the name of the button (the text that is supposed to be displayed ontop)
        x = start_buttons[dictkeys[i]][1] #Get the x value from dict at dictkeys
        y = start_buttons[dictkeys[i]][2] #Get the y value from dict at dictkeys
        widthx = start_buttons[dictkeys[i]][3] #Get the width x from dict at dictkeys
        heighty = start_buttons[dictkeys[i]][4] #Get the height y from the dict at dictkeys    
     
        
        
    #Draw the start buttons
        fill(255)
        rectMode(CENTER)
        rect(x, y, widthx, heighty)
        
        fill(0)
        textSize(30)
        textAlign(CENTER)
        text(button_name, x, y)
        
    #Write instructions
        fill(0)
        textSize(15)
        text("To select a word, your first click must be at the starting letter ", 720/2, 50)
        text("of the word and the second click must be at the ending letter of the word.", 720/2, 75)
        text("Click a button above to choose difficulty of the Word Search", 720/2, 670)
        
    #Set boundaries for the active buttons
    
    active_buttons = {
        "easy" : ["Easy Map", 260, 100, 460, 200],
        "medium" : ["Medium Map", 260, 300, 460, 400],
        "hard" : ["Hard Map", 260, 500, 460, 600] 
            # array format in ["name of button", top left cornerx, top left cornery, bottom right cornerx, bottom right cornery]
        }    
    
    #Check if button is pressed matches to possible buttons to change game state
    
    expected_button_presses = ["Easy Map", "Medium Map", "Hard Map"]
    possible_game_states = ["easy_map", "medium_map", "hard_map"]
    
    for i in range(len(expected_button_presses)):
        if current_button_pressed == expected_button_presses[i]:
            game_state = possible_game_states[i]
            current_level_name = current_button_pressed

def screenDivider(rows, cols, screenwidth, screenheight):
    squarewidth = screenwidth / rows 
    squareheight = screenheight / cols
    return squarewidth, squareheight


def squareDrawer(squarewidth, squareheight, rows, cols): #Draws the squares for the word search
    fill(255)
    stroke(0)
    rectMode(CORNER)
    for i in range(rows):
        for j in range(cols):
            rect(squarewidth * j, squareheight * i, squarewidth, squareheight)
def checkWinCondition():
    global answer_bank, game_state
    if len(answer_bank) == 0:
        game_state = "winner_menu"
            
def textDrawer(squarewidth, squareheight, rows, cols, textarr): #Draws the letters for the word search
    fill(0)
    stroke(0)
    textAlign(BOTTOM)
    textSize(20)
    for i in range(rows):
        for j in range(cols):
            text(map_arr[i][j], squarewidth * j + squarewidth/2, squareheight * i + squareheight/2)

def wordBankDrawer(word_bank):
    textAlign(CENTER)
    textSize(15)
    text(word_bank, 720/2, 780)

def answerSelectDrawer(current_coords, squarewidth, squareheight, rows, cols):
    fill(0)
    stroke(100)
    strokeWeight(5)
    line(squarewidth * current_coords[0][0] + squarewidth/2, squareheight * current_coords[0][1]+ squarewidth/2, 
            squarewidth * current_coords[1][0] + squarewidth/2, squareheight * current_coords[1][1]+ squarewidth/2)
    strokeWeight(1)
    
    
def board_drawer(square_dimensions, rows, cols, map_arr):
    global board_drawn
    if board_drawn == False:
        squareDrawer(square_dimensions[0], square_dimensions[1], rows, cols)
        textDrawer(square_dimensions[0], square_dimensions[1], rows, cols, map_arr)
        wordBankDrawer(word_bank)
        board_drawn = True
                                                                        
def boundaryCreator(squarewidth, squareheight, rows, cols): 
    global active_square_buttons, square_boundaries_made
#Creates a 3D of which the i is the y value and the j is the x value of the square pressed, contained in the value arr[i][j] are the top left and bottom right corners of the square
    if square_boundaries_made == False:
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append([squarewidth * j, squareheight * i, squarewidth * j + squarewidth , squareheight * i + squareheight])
            active_square_buttons.append(row)
        square_boundaries_made = True

def createEmptyMap(mapheight, mapwidth):
    arr = []
    for i in range(mapheight):
            row = []
            for j in range(mapwidth):
                row.append(None)
            arr.append(row)
    return arr

def placeWord(currentmap, word):
    global answer_bank

    mapheight, mapwidth = len(currentmap), len(currentmap[0])
    directions = [(1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (-1, 1), (1, -1), (-1, -1)]
    random.shuffle(directions)
    
    while True:
        answer_bank_current = []
        direction = random.choice(directions)
        currentrow, currentcol = random.randint(0, mapheight - 1), random.randint(0, mapwidth - 1) #substract 1 because arrays start at 0
        startingrow, startingcol = currentrow, currentcol
        word_fits = True
        
        for letter in word:
            if ((0 <= currentrow) and currentrow <= (mapheight - 1)) and ((0 <= currentcol) and currentcol <= (mapwidth - 1)) and (currentmap[currentrow][currentcol] == None or currentmap[currentrow][currentrow] == letter):
                currentcol += direction[0]
                currentrow += direction[1]
            else:
                word_fits = False
                break
        
        if word_fits == True:
            answer_bank_current.append([startingcol, startingrow])
            for letter in word:
                # print(currentrow, currentcol)
                currentmap[startingrow][startingcol] = letter
                startingcol += direction[0]
                startingrow += direction[1]
            startingcol -= direction[0]
            startingrow -= direction[1]
            answer_bank_current.append([startingcol, startingrow]) 
            answer_bank.append(answer_bank_current)
            return (True, currentmap)
        return (False, currentmap)
    
def mapCreator(word_list, map_height, map_width):
    global map_arr
    while len(word_list) != 0:
        for word in word_list:
            map_state_array = placeWord(map_arr, word)
            if map_state_array[0] == False:
                continue
            elif map_state_array[0] == True:
                map_arr = map_state_array[1]
                word_list.remove(word)
    fill_empty_spaces()
    
def fill_empty_spaces():
    global map_arr
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(len(map_arr)):
        for j in range(len(map_arr[i])):
            if map_arr[i][j] == None:
                map_arr[i][j] = random.choice(letters)        

def easyMap():
    global window_info, active_square_buttons, map_arr, word_bank, answer_bank, current_coordinate_pressed
    global board_drawn, intialized_answer_bank
    
    rows, cols = 7, 7
    word_bank = "BANANA, MOON, RAIN, QUEEN, CHAIR"
    word_list = ["BANANA", "MOON", "RAIN", "QUEEN", "CHAIR"]
    if intialized_answer_bank == False:
        answer_bank = []
        map_arr = createEmptyMap(rows, cols)
        mapCreator(word_list, rows, cols)
        intialized_answer_bank = True
    #Draw the squares for the crossword board
    
    square_dimensions = screenDivider(rows, cols, window_info["width"], window_info["height"])
    
    board_drawer(square_dimensions, rows, cols, map_arr)
    
    boundaryCreator(square_dimensions[0], square_dimensions[1], rows, cols)

    if currentCoordinateChecker(current_coordinate_pressed) == True:
        answerSelectDrawer(current_coordinate_pressed, square_dimensions[0], square_dimensions[1], rows, cols)
                                                                
def mediumMap():
    global window_info, active_square_buttons, map_arr, word_bank, answer_bank, current_coordinate_pressed
    global board_drawn, intialized_answer_bank
    
    rows, cols = 9, 9
    word_bank = "MUSIC, BUS, TABLE, FLOWER, SUN, BAT, CHERRY, TIGER, DUCK, FOX"
    word_list = ["MUSIC", "BUS", "TABLE", "FLOWER", "SUN", "BAT", "CHERRY", "TIGER", "DUCK", "FOX"]
    if intialized_answer_bank == False:
        answer_bank = []
        map_arr = createEmptyMap(rows, cols)
        mapCreator(word_list, rows, cols)
        intialized_answer_bank = True
    #Draw the squares for the crossword board
    
    square_dimensions = screenDivider(rows, cols, window_info["width"], window_info["height"])
    
    board_drawer(square_dimensions, rows, cols, map_arr)
    
    boundaryCreator(square_dimensions[0], square_dimensions[1], rows, cols)

    if currentCoordinateChecker(current_coordinate_pressed) == True:
        answerSelectDrawer(current_coordinate_pressed, square_dimensions[0], square_dimensions[1], rows, cols)
                 
def hardMap():
    global window_info, active_square_buttons, map_arr, word_bank, answer_bank, current_coordinate_pressed
    global board_drawn, intialized_answer_bank
    
    rows, cols = 12, 12
    word_bank = "TREE, FOX, BEACH, BANANA, CAKE, FISH, PEN, CHAIR, TIGER, HOUSE, RAIN, QUEEN, CAT, DOG, BIRD"
    word_list = ['TREE', 'FOX', 'BEACH', 'BANANA', 'CAKE', 'FISH', 'PEN', 'CHAIR', 'TIGER', 'HOUSE',
                  'RAIN', 'QUEEN', 'CAT', 'DOG', 'BIRD']

    if intialized_answer_bank == False:
        answer_bank = []
        map_arr = createEmptyMap(rows, cols)
        mapCreator(word_list, rows, cols)
        intialized_answer_bank = True
    #Draw the squares for the crossword board
    
    square_dimensions = screenDivider(rows, cols, window_info["width"], window_info["height"])
    
    board_drawer(square_dimensions, rows, cols, map_arr)
    
    boundaryCreator(square_dimensions[0], square_dimensions[1], rows, cols)

    if currentCoordinateChecker(current_coordinate_pressed) == True:
        answerSelectDrawer(current_coordinate_pressed, square_dimensions[0], square_dimensions[1], rows, cols)

def winnerMenu():
    global current_level_name, window_info
    
    rectMode(CORNER)
    fill(255)
    rect(0,0, 1000, 1000)
    
    fill(0)
    textAlign(CENTER)
    textSize(40)
    winner_message = "You beat the " + current_level_name + "!"
    x, y = window_info["width"]/2, window_info["height"]/2
    text("Congrats!", x, y - 50)
    text(str(winner_message), x,y)
        
def setup():
    global game_state 
    global window_info
    global buttons, active_square_buttons, square_boundaries_made
    global current_button_pressed, current_coordinate_pressed
    global map_arr
    global word_bank
    global board_drawn
    global intialized_answer_bank
    
    game_state = "start_menu"
    
    window_info = {
                   "width" : 720,
                   "height" : 720
                   }

    current_button_pressed = None
    current_coordinate_pressed = [None, None]
    
    active_square_buttons = []
    square_boundaries_made = False
    
    board_drawn = False
    intialized_answer_bank = False
    
    word_bank = ""
    
    current_level_name = ""
    
    size (720, 820)
    background(200,200,200)
    
def draw():
    global game_state, current_button_pressed, board_drawn, map_arr
    if game_state == "start_menu":
        startMenu()

    elif game_state == "easy_map":
        easyMap()
        checkWinCondition()

    elif game_state == "medium_map":
        mediumMap()
        checkWinCondition()

    elif game_state == "hard_map":
        hardMap()
        checkWinCondition()
    elif game_state == "winner_menu":
        winnerMenu()

import cards

def setup():
    """
    paramaters: None (deck can be created within this function)
    returns:
    - a foundation (list of 4 empty lists)
    - cell (list of 4 empty lists)
    - a tableau (a list of 8 lists, the dealt cards)
    """
    deck = cards.Deck()
    deck.shuffle()
    
    foundation = [[],[],[],[]] # temporary value that needs to be replaced
    cell = [[],[],[],[]] # temporary value that needs to be replaced  
    tableau = [[],[],[],[],[],[],[],[]] # temporary value that needs to be replaced
    col = 0
    while not deck.is_empty():
        tableau[col].append(deck.deal())
        col += 1
        if col % 8 == 0:
            col = 0 
    return foundation,tableau,cell


def move_to_foundation(tableau,foundation,t_col,f_col):
    '''
    parameters: a tableau, a foundation, column of tableau, column of foundation
    returns: Boolean (True if the move is valid, False otherwise)
    moves a card at the end of a column of tableau to a column of foundation
    This function can also be used to move a card from cell to foundation
    '''
    if t_col >= 0 and t_col <= 7 and f_col >= 0 and f_col <= 3:
        card_rank = tableau[t_col][-1].get_rank()
        card_suit = tableau[t_col][-1].get_suit()
        if len(foundation[f_col]) == 0:
            if card_rank == 1:
                return True
        elif foundation[f_col][-1].get_suit() == card_suit:
            if foundation[f_col][-1].get_rank()+1 == card_rank:
                return True
    return False

def move_to_cell(tableau,cell,t_col,c_col):
    '''
    parameters: a tableau, a cell, column of tableau, column of cell
    returns: Boolean (True if the move is valid, False otherwise)
    moves a card at the end of a column of tableau to a cell
    '''
    if t_col >= 0 and t_col <= 7 and c_col >= 0 and c_col <= 3:
        if len(cell[c_col]) == 0:
                return True
    return False

def move_to_tableau(tableau,cell,t_col,c_col):
    '''
    parameters: a tableau, a cell, column of tableau, a cell
    returns: Boolean (True if the move is valid, False otherwise)
    moves a card in the cell to a column of tableau
    remember to check validity of move
    '''
    if t_col >= 0 and t_col <= 7 and c_col >= 0 and c_col <= 3:
        t_card_rank = tableau[t_col][-1].get_rank()
        t_card_suit = tableau[t_col][-1].get_suit()
        c_card_rank = cell[c_col][0].get_rank()
        c_card_suit = cell[c_col][0].get_suit()
        if len(cell[c_col]) == 0:
            return False
        elif (c_card_suit % 2) != (t_card_suit % 2):
            if c_card_rank + 1 == t_card_rank:
                return True
    return False
 
 
        

def is_winner(foundation):
    '''
    parameters: a foundation
    return: Boolean
    '''
    did_they_win = False
    for x in range(len(foundation)):
        if len(foundation[x]) != 0:
            did_they_win = True
        else:
            return False
    return did_they_win


def move_in_tableau(tableau,t_col_source,t_col_dest):
    '''
    parameters: a tableau, the source tableau column and the destination tableau column
    returns: Boolean
    move card from one tableau column to another
    remember to check validity of move
    '''
    if t_col_source >= 0 and t_col_source <= 7 and t_col_dest >= 0 and t_col_dest <= 3:
        source_card_rank = tableau[t_col_source][-1].get_rank()
        source_card_suit = tableau[t_col_source][-1].get_suit()
        dest_card_rank = tableau[t_col_dest][-1].get_rank()
        dest_card_suit = tableau[t_col_dest][-1].get_suit()
        if len(tableau[t_col_dest]) == 0:
            if source_card_rank == 13:
                return True
        elif (source_card_suit % 2) != (dest_card_suit % 2):
            if dest_card_rank - 1 == source_card_rank:
                return True
    return False
        

def print_game(foundation, tableau,cell):
    """
    parameters: a tableau, a foundation and a cell
    returns: Nothing
    prints the game, i.e, print all the info user can see.
    Includes:
        a) print tableau  
        b) print foundation ( can print the top card only)
        c) print cells

    """
    print()
    print("                 Cells:                              Foundation:")
    # print cell and foundation labels in one line
    for i in range(4):
        print('{:8d}'.format(i+1), end = '')
    print('    ', end = '')
    for i in range(4):
        print('{:8d}'.format(i+1), end = '')
    print()  # carriage return at the end of the line
    print('{:6s}'.format(''), end = '')
    # print cell and foundation cards in one line; foundation is only top card
    for c in cell:
        # print if there is a card there; if not, exception prints spaces.
        try:
            temp = str(c[0])
            print('{:<7s}'.format(temp), end = '')
        except IndexError:
            print('{:<8s}'.format(''), end = '')
            
    print('    ', end = '')
    for stack in foundation:
        # print if there is a card there; if not, exception prints spaces.
        try:
            temp = str(stack[-1])
            print('{:<8s}'.format(temp), end = '')
        except IndexError:
            print('{:<9s}'.format(''), end = '')

    print()  # carriage return at the end of the line
    print('----------')

    print("Tableau")
    for i in range(len(tableau)):  # print tableau headers
        print('{:8d}'.format(i + 1), end = '')
    print()  # carriage return at the end of the line

    # Find the length of the longest stack
    max_length = max([len(stack) for stack in tableau])

    # print tableau stacks row by row
    for i in range(max_length):  # for each row
        print(' '*7, end = '')  # indent each row
        for stack in tableau:
            # print if there is a card there; if not, exception prints spaces.
            try:
                temp = str(stack[i])
                print('{:8s}'.format(temp), end = '')
            except IndexError:
                print('{:8s}'.format(''), end = '')
        print()  # carriage return at the end of the line
    print('----------')

def print_rules():
    '''
    parameters: none
    returns: nothing
    prints the rules
    '''
    print("Rules of FreeCell")

    print("Goal")
    print("\tMove all the cards to the Foundations")

    print("Foundation")
    print("\tBuilt up by rank and by suit from Ace to King")

    print("Tableau")
    print("\tBuilt down by rank and by alternating color")
    print("\tThe bottom card of any column may be moved")
    print("\tAn empty spot may be filled with any card ")

    print("Cell")
    print("\tCan only contain 1 card")
    print("\tThe card may be moved")

def show_help():
    '''
    parameters: none
    returns: nothing
    prints the supported commands
    '''
    print("Responses are: ")
    print("\t t2f #T #F - move from Tableau to Foundation")
    print("\t t2t #T1 #T2 - move card from one Tableau column to another")
    print("\t t2c #T #C - move from Tableau to Cell")
    print("\t c2t #C #T - move from Cell to Tableau")
    print("\t c2f #C #F - move from Cell to Foundation")
    print("\t 'h' for help")
    print("\t 'q' to quit")    
    
def play():
    ''' 
    Main program. Does error checking on the user input. 
    '''
    print_rules()
    foundation, tableau, cell = setup() 
       
    show_help()
    choice_q = False
    while not choice_q:
        # Uncomment this next line. It is commented out because setup doesn't do anything so printing doesn't work.
        print_game(foundation, tableau, cell)
        if is_winner(foundation):
            print('You Win!')
            break
        response = input("Command (type 'h' for help): ")
        response = response.strip()
        response_list = response.split()
        if len(response_list) > 0:
            r = response_list[0]
            try:
                if r == 't2f':
                    t = int(input('Enter tableau column: ')) - 1
                    f = int(input('Enter foundation column: ')) -1
                    if move_to_foundation(tableau, foundation, t,f):
                        foundation[f].append(tableau[t].pop())
                    else:
                        print('\n*** INVALID MOVE ***\n')
                        
                elif r == 't2t':
                    t_source = int(input('Enter tableau source column: ')) - 1
                    t_dest = int(input('Enter tableau destination column: ')) - 1
                    if move_in_tableau(tableau, t_source,t_dest):
                        tableau[t_dest].append(tableau[t_source][-1])
                        tableau[t_source].pop()
                    else:
                        print('\n*** INVALID MOVE ***\n') 
                            
                elif r == 't2c':
                    t = int(input('Enter tableau column: ')) - 1
                    c = int(input('Enter cell column: ')) -1
                    if move_to_cell(tableau, cell, t,c):
                        cell[c].append(tableau[t].pop())
                    else:
                        print('\n*** INVALID MOVE ***\n')
                             
                elif r == 'c2t':
                    c = int(input('Enter cell column: ')) - 1
                    t = int(input('Enter tableau column: ')) - 1
                    if move_to_tableau(tableau,cell,t,c):
                        tableau[t].append(cell[c].pop())
                    else:
                        print('\n*** INVALID MOVE ***\n')
                              
                elif r == 'c2f':
                    c = int(input('Enter cell column: ')) - 1
                    f = int(input('Enter foundation column: ')) - 1
                    if move_to_foundation(cell,foundation,c,f):
                        foundation[f].append(cell[c].pop())
                    else:
                        print('\n*** INVALID MOVE ***\n')                         
                elif r == 'q':
                    choice_q = True
                elif r == 'h':
                    show_help()
                else:
                    print('Unknown command:',r)
            except ValueError:
                print('Invalid input, you must use integer numbers for your moves.')
        else:
            print("Unknown Command:",response)
    print('Thanks for playing')

play()


        
    


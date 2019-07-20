from copy import deepcopy

class output_Class(object):
    count = 0
    value = 0
    stateOfBoard = list()
    
    def __init__(self,value=0,count=0,inputList=list(),outputList=list()):
        self.count = count
        self.value = value
        self.inputList = inputList
        self.outputList = outputList
 
    
# Input: a board position
# Output: a list L of board positions
# Return the list produced by GenerateAdd applied to the board
def gen_Move_Opening(postionOfBoard):
    board_Position = generateAdd(postionOfBoard)
    return board_Position

def gen_MoveOpening_Black(board_input):
    moves_black = generateAdd(boardFlip(board_input))
    movesList = list()
    
    for each in range(0,len(moves_black)):
        board = moves_black[each]
        movesList.insert(each,boardFlip(board))
    return movesList 

# for black opening
def boardFlip(inputToFlip):
    board = list(range(0,23))
    for i in range(0,len(inputToFlip)):
        if(inputToFlip[i]=='B'):
            board[i]='W'
        elif(inputToFlip[i]=='W'):
            board[i]='B'
        else:
            board[i]='x'
    return board

# Input: a location j in the array representing the board and the board b
# Output: true if the move to j closes a mill
def closeMill(position,board):
    boardValue = board[position]
    if(boardValue=='x'):
        return False
    else:
        return checkMills(position,board,boardValue)

#White Mill case
def checkMills(position,board,boardValue):
    if(boardValue=='x'):

        return False
    if position == 0:
        if (board[1] == boardValue and board[2] == boardValue) or (board[3] == boardValue and board[6] == boardValue) or (board[8] == boardValue and board[20] == boardValue):
            return True
        else:
            return False
    elif position == 1:
        if(board[0] == boardValue and board[2] == boardValue):
            return True
        else:
            return False
    elif position == 2:
        if (board[0] == boardValue and board[1] == boardValue) or (board[5] == boardValue and board[7] == boardValue) or (board[13] == boardValue and board[22] == boardValue):
            return True
        else:
            return False
    elif position == 3:
        if (board[0] == boardValue and board[6] == boardValue) or (board[4] == boardValue and board[5] == boardValue) or (board[9] == boardValue and board[17] == boardValue):
            return True
        else:
            return False
    elif position == 4:
        if (board[3] == boardValue and board[5] == boardValue):
            return True
        else:
            return False
    elif position == 5:
        if (board[3] == boardValue and board[4] == boardValue) or (board[2] == boardValue and board[7] == boardValue) or (board[12] == boardValue and board[19] == boardValue):
            return True
        else:
            return False
    elif position == 6:
        if (board[0] == boardValue and board[3] == boardValue) or (board[10] == boardValue and board[14] == boardValue):
            return True
        else:
            return False
    elif position == 7:
        if (board[2] == boardValue and board[5] == boardValue) or (board[11] == boardValue and board[16] == boardValue):
            return True
        else:
            return False
    elif position == 8:
        if (board[0] == boardValue and board[20] == boardValue) or (board[9] == boardValue and board[10] == boardValue):
            return True
        else:
            return False
    elif position == 9:
        if (board[8] == boardValue and board[10] == boardValue) or (board[3] == boardValue and board[17] == boardValue):
            return True
        else:
            return False
    elif position == 10:
        if (board[8] == boardValue and board[9] == boardValue) or (board[6] == boardValue and board[14] == boardValue):
            return True
        else:
            return False
    elif position == 11:
        if (board[7] == boardValue and board[16] == boardValue) or (board[12] == boardValue and board[13] == boardValue):
            return True
        else:
            return False
    elif position == 12:
        if (board[11] == boardValue and board[13] == boardValue) or (board[5] == boardValue and board[19] == boardValue):
            return True
        else:
            return False
    elif position == 13:
        if (board[11] == boardValue and board[12] == boardValue) or (board[2] == boardValue and board[22] == boardValue):
            return True
        else:
            return False
    elif position == 14:
        if (board[15] == boardValue and board[16] == boardValue) or (board[6] == boardValue and board[10] == boardValue) or (board[17] == boardValue and board[20] == boardValue):
            return True
        else:
            return False
    elif position == 15:
        if (board[14] == boardValue and board[16] == boardValue) or (board[18] == boardValue and board[21] == boardValue):
            return True
        else:
            return False
    elif position == 16:
        if (board[14] == boardValue and board[15] == boardValue) or (board[7] == boardValue and board[11] == boardValue) or (board[19] == boardValue and board[22] == boardValue):
            return True
        else:
            return False
    elif position == 17:
        if (board[14] == boardValue and board[20] == boardValue) or (board[3] == boardValue and board[9] == boardValue) or (board[18] == boardValue and board[19] == boardValue):
            return True
        else:
            return False
    elif position == 18:
        if (board[15] == boardValue and board[21] == boardValue) or (board[17] == boardValue and board[19] == boardValue):
            return True
        else:
            return False
    elif position == 19:
        if (board[17] == boardValue and board[18] == boardValue) or (board[5] == boardValue and board[12] == boardValue) or (board[16] == boardValue and board[22] == boardValue):
            return True
        else:
            return False
    elif position == 20:
        if (board[0] == boardValue and board[8] == boardValue) or (board[14] == boardValue and board[17] == boardValue) or (board[21] == boardValue and board[22] == boardValue):
            return True
        else:
            return False
    elif position == 21:
        if (board[20] == boardValue and board[22] == boardValue) or (board[15] == boardValue and board[18] == boardValue):
            return True
        else:
            return False
    elif position == 22:
        if (board[20] == boardValue and board[21] == boardValue) or (board[16] == boardValue and board[19] == boardValue) or (board[2] == boardValue and board[13] == boardValue):
            return True
        else:
            return False
    else:
        return False

    
# Input: a board position and a list L
# Output: positions are added to L by removing black pieces
def generateRemove(position_Board,in_list):
    for i in range(0,len(position_Board)):
        if position_Board[i]=='B':
            if(closeMill(i,position_Board)==False):
                updatedBoard = deepcopy(position_Board)   
                updatedBoard[i]='x'
                in_list.append(updatedBoard)
    return in_list


# Input: a board position
# Output: a list L of board positions
def generateAdd(positionInBoard):
    b_positionList = list()
    for i in range(0,len(positionInBoard)):
        if(positionInBoard[i]=='x'):
            temp_board = deepcopy(positionInBoard)
            temp_board[i]='W'
            if (closeMill(i,temp_board)):
                b_positionList = generateRemove(temp_board,b_positionList)
            else:
                b_positionList.append(temp_board)
    return b_positionList

# Input: a location j in the array representing the board
# Output: a list of locations in the array corresponding to j’s neighbors
def neighbors(positionInBoard):
    list_Neighbors = list()
    
    if(positionInBoard==0):
        list_Neighbors.append(8)
        list_Neighbors.append(3)
        list_Neighbors.append(1)
        
    elif(positionInBoard==1):
        list_Neighbors.append(4)
        list_Neighbors.append(2)
        list_Neighbors.append(0)
        
    elif(positionInBoard==2):
        list_Neighbors.append(13)
        list_Neighbors.append(5)
        list_Neighbors.append(1)
        
    elif(positionInBoard==3):
        list_Neighbors.append(9)
        list_Neighbors.append(6)
        list_Neighbors.append(4)
        list_Neighbors.append(0)
        
    elif(positionInBoard==4):
        list_Neighbors.append(5)
        list_Neighbors.append(3)
        list_Neighbors.append(1)
        
    elif(positionInBoard==5):
        list_Neighbors.append(12)
        list_Neighbors.append(7)
        list_Neighbors.append(4)
        list_Neighbors.append(2)

    elif(positionInBoard==6):
        list_Neighbors.append(10)
        list_Neighbors.append(7)
        list_Neighbors.append(3)
    
    elif(positionInBoard==7):
        list_Neighbors.append(11)
        list_Neighbors.append(6)
        list_Neighbors.append(5)
    
    elif(positionInBoard==8):
        list_Neighbors.append(20)
        list_Neighbors.append(9)
        list_Neighbors.append(0)
        
    elif(positionInBoard==9):
        list_Neighbors.append(17)
        list_Neighbors.append(10)
        list_Neighbors.append(8)
        list_Neighbors.append(3)
        
    elif(positionInBoard==10):
        list_Neighbors.append(14)
        list_Neighbors.append(9)
        list_Neighbors.append(6)
        
    elif(positionInBoard==11):
        list_Neighbors.append(16)
        list_Neighbors.append(12)
        list_Neighbors.append(7)
        
    elif(positionInBoard==12):
    	list_Neighbors.append(19)
        list_Neighbors.append(13)
        list_Neighbors.append(11)
        list_Neighbors.append(5)
       
    elif(positionInBoard==13):
        list_Neighbors.append(22)
        list_Neighbors.append(12)
        list_Neighbors.append(2)
     
    elif(positionInBoard==14):
        list_Neighbors.append(17)
        list_Neighbors.append(15)
        list_Neighbors.append(10)
        
    elif(positionInBoard==15):
        list_Neighbors.append(18)
        list_Neighbors.append(16)
        list_Neighbors.append(14)
        
    elif(positionInBoard==16):
        list_Neighbors.append(19)
        list_Neighbors.append(15)
        list_Neighbors.append(11)
        
    elif(positionInBoard==17):
    	list_Neighbors.append(20)
    	list_Neighbors.append(18)
        list_Neighbors.append(14)
        list_Neighbors.append(9)

    elif(positionInBoard==18):
    	list_Neighbors.append(21)
        list_Neighbors.append(19)
        list_Neighbors.append(17)
        list_Neighbors.append(15)

    elif(positionInBoard==19):
    	list_Neighbors.append(22)
        list_Neighbors.append(18)
        list_Neighbors.append(16)
        list_Neighbors.append(12)
        
    elif(positionInBoard==20):
    	list_Neighbors.append(21)
        list_Neighbors.append(17)
        list_Neighbors.append(8)

    elif(positionInBoard==21):
        list_Neighbors.append(22)
        list_Neighbors.append(20)
        list_Neighbors.append(18)

    elif(positionInBoard==22):
        list_Neighbors.append(21)
        list_Neighbors.append(19)
        list_Neighbors.append(13)
    
    else:
        return list_Neighbors
        
    return list_Neighbors

# Input: a board position
# Output: a list L of board positions
def generateMove(positionInBoard):
    position_List = list()

    for pos in range(0,len(positionInBoard)):
        if(positionInBoard[pos]=='W'):
            n = neighbors(pos)
            for j in n:
                if(positionInBoard[j]=='x'):
                    tempBoard = deepcopy(positionInBoard)
                    tempBoard[pos]='x'
                    tempBoard[j]='W'
                    if(closeMill(j,tempBoard)):
                        position_List = generateRemove(tempBoard,position_List)
                    else:
                        position_List.append(tempBoard)
    return position_List
                     

# Input: a board position
# Output: a list L of board positions
def generateMovesMidgameEndgame(positionInBoard):
    white_Count = 0
    L = list()
    for position in range(0,len(positionInBoard)):
        if(positionInBoard[position]=='W'):
            white_Count = white_Count+1
    
    if(white_Count==3):
        L = generateHopping(positionInBoard)
    else:
        L = generateMove(positionInBoard)
    return L

def generateMovesMidgameEndgameBlack(positionInBoard):
    tempBoard = boardFlip(positionInBoard)
    List = list()
    position_List = generateMovesMidgameEndgame(tempBoard)
    for pos in range(0,len(position_List)):
        b = position_List[pos]
        List.insert(pos,boardFlip(b))
    return List
    
def generateHopping(positionInBoard):
    position_List = list()
    for alpha in range(0,len(positionInBoard)):
        if(positionInBoard[alpha]=='W'):
            for beta in range(0,len(positionInBoard)):
                if (positionInBoard[beta]=='x'):
                    tempBoard = deepcopy(positionInBoard)
                    tempBoard[alpha]='x'
                    tempBoard[beta]='W'
                    if(closeMill(beta,tempBoard)):
                        position_List = generateRemove(tempBoard,position_List)
                    else:
                        position_List.append(tempBoard)
    return position_List
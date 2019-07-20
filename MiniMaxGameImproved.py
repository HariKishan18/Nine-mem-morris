import sys
import BoardLogic

maximum_Value = sys.maxsize
minimum_Value = -sys.maxsize
depth = int(sys.argv[3])
board = list()

#Reading board input state
def get_Board_State():
    board3 = open(sys.argv[1],"r")
    board = list()
    for line in board3:
        for char in line:
            board.append(char)
    return board



def MiniMaxGameImproved(depth,board,flag):
    out = BoardLogic.output_Class()
    inp = BoardLogic.output_Class()
    boardList = list()
    if(depth==0):
        noOfWhite = 0
        noOfBlack = 0
        
        for pos in range(0,len(board)):
            if(board[pos]=='W'):
                noOfWhite= noOfWhite+1
            elif(board[pos]=='B'):
                noOfBlack = noOfBlack+1   
                
        difference = 0
        mills_count = 0
        staticEstimate = 0
        difference = noOfWhite-noOfBlack
        
        for each in range(0,len(board)):
            if(board[each]=='x'):
                if(BoardLogic.checkMills(each,board,'W')==True):
                    mills_count = mills_count+1
        
        staticEstimate = difference + mills_count
        movesList = BoardLogic.generateMovesMidgameEndgameBlack(board)
        movesList_size = len(movesList)
        
        if(noOfBlack<=2):
            out.value = 10000
        elif(noOfWhite<=2):
            out.value = -10000
        elif(movesList_size==0):
            out.value = 10000
        else:
            out.value = 1000*(staticEstimate) - movesList_size
        out.count +=1
        return out
    
    if(flag==1):
        boardList = BoardLogic.generateMovesMidgameEndgame(board)
        out.value = minimum_Value
    else:
        boardList = BoardLogic.generateMovesMidgameEndgameBlack(board)
        out.value = maximum_Value
        
    for bpos in boardList:
        if(flag==1):
            inp = MiniMaxGameImproved(depth-1,bpos,0)
            if(inp.value>out.value):
                out.value=inp.value
                out.boardState = bpos
            out.count = out.count + inp.count
            
        else:
            inp = MiniMaxGameImproved(depth-1,bpos,1)
            if(inp.value<out.value):
                out.value=inp.value
                out.boardState = bpos
            out.count = out.count + inp.count         
    return out

def write_Board_State(outBoardState):
    board4 = open(sys.argv[2],"w+")
    for each in outBoardState:
        board4.write(each)
    board4.close()
    
def output_State():
    board = list()
    board1 = open(sys.argv[2], "r")
    for line in board1:
        for char in line:
            board.append(char)
    board1.close()
    return board


board = get_Board_State()  
output = MiniMaxGameImproved(depth,board,1)
print("Input position",''.join(get_Board_State()))
write_Board_State(output.boardState)
print("Output Position:", ''.join(output_State()))
print("Position evaluated by static estimation:",output.count)
print("MINIMAX esitmate:",output.value)

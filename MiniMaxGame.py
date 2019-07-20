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

def write_Board_State(outBoardState):
    board4 = open(sys.argv[2],"w+")
    for each in outBoardState:
        board4.write(each)
    board4.close()


def output_State():
    board = list()
    board3 = open(sys.argv[2], "r")
    for line in board3:
        for char in line:
            board.append(char)
    board3.close()
    return board

def MiniMaxGame(depth,board,flag):
    out = BoardLogic.output_Class()
    inp = BoardLogic.output_Class()
#    boardList = list()
    if(depth==0):
        noOfWhite = 0
        noOfBlack = 0
        total_Count_final = 0
        for pos in range(0,len(board)):
            if(board[pos]=='W'):
                noOfWhite= noOfWhite+1
            elif(board[pos]=='B'):
                noOfBlack = noOfBlack+1
                
        total_Count_final = noOfWhite-noOfBlack
        midgame_List = BoardLogic.generateMovesMidgameEndgameBlack(board)
        midgame_List_size = len(midgame_List)
        
        if(noOfBlack<=2):
            out.value = 10000
        elif(noOfWhite<=2):
            out.value = -10000
        elif(midgame_List_size==0):
            out.value = 10000
        else:
            out.value = 1000*(total_Count_final) - midgame_List_size
        out.count +=1
        out.boardState = board
        return out
    
    boardList = list()
    if(flag==1):
        boardList = BoardLogic.generateMovesMidgameEndgame(board)
        out.value = minimum_Value
    else:
        boardList = BoardLogic.generateMovesMidgameEndgameBlack(board)
        out.value = maximum_Value
        
    for bPos in boardList:
        if(flag==1):
            inp = MiniMaxGame(depth-1,bPos,0)
            if(inp.value>out.value):
                out.value=inp.value
                out.boardState = bPos
            out.count = out.count + inp.count
            
        else:
            inp = MiniMaxGame(depth-1,bPos,1)
            if(inp.value<out.value):
                out.value=inp.value
                out.boardState = bPos
            out.count = out.count + inp.count         
    return out

board = get_Board_State()  
output = MiniMaxGame(depth,board,1)
print("Input position",''.join(get_Board_State()))
write_Board_State(output.boardState)
print("Output Position:", ''.join(output_State()))
print("Position evaluated by static estimation:",output.count)
print("MINIMAX esitmate:",output.value)


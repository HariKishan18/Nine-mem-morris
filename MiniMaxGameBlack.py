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
    board1 = open(sys.argv[2], "r")
    for line in board1:
        for char in line:
            board.append(char)
    board1.close()
    return board
    
def MiniMaxGameBlack(depth,gameBoard,flag):
    out = BoardLogic.output_Class()
    inp = BoardLogic.output_Class()
    boardList = list()
    if(depth==0):
        noOfWhite = 0
        noOfBlack = 0
        for i in range(0,len(gameBoard)):
            if(gameBoard[i]=='W'):
                noOfWhite+=1
            elif(gameBoard[i]=='B'):
                noOfBlack+=1
                
        total_Count_final = noOfBlack-noOfWhite
        moves_List = BoardLogic.generateMovesMidgameEndgame(gameBoard)
        moves_List_size = len(moves_List)
        if(noOfBlack<=2):
            out.value = 10000
        elif(noOfWhite<=2):
            out.value = -10000
        elif(moves_List_size==0):
            out.value = 10000
        else:
            out.value = 1000*(total_Count_final) - moves_List_size
        out.count +=1
        return out
    
    if(flag==1):
        boardList = BoardLogic.generateMovesMidgameEndgameBlack(gameBoard)
        out.value = minimum_Value
    else:
        boardList = BoardLogic.generateMovesMidgameEndgame(gameBoard)
        out.value = maximum_Value
        
    for bpos in boardList:
        if(flag==1):
            inp = MiniMaxGameBlack(depth-1,bpos,0)
            if(inp.value>out.value):
                out.value=inp.value
                out.boardState = bpos
            out.count = out.count + inp.count
            
        else:
            inp = MiniMaxGameBlack(depth-1,bpos,1)
            if(inp.value<out.value):
                out.value=inp.value
                out.boardState = bpos
            out.count = out.count + inp.count
            
    return out

board = get_Board_State()  
output = MiniMaxGameBlack(depth,board,1)
print("Input position",''.join(get_Board_State()))
write_Board_State(output.boardState)
print("Output Position:", ''.join(output_State()))
print("Position evaluated by static estimation:",output.count)
print("MINIMAX esitmate:",output.value)

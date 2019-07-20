import sys
import BoardLogic

maximum_Value = sys.maxsize
minimum_Value = -sys.maxsize
depth = int(sys.argv[3])
boardState = list()

#Reading board input state
def get_Board_State():
    board1 = open(sys.argv[1],"r")
    board = list()
    for data in board1:
        for char in data:
            board.append(char)
    board1.close()
    return board

def write_Board_State(outBoardState):
    board2 = open(sys.argv[2],"w+")
    for each in outBoardState:
        board2.write(each)
    board2.close()


def output_State():
    board = list()
    board1 = open(sys.argv[2], "r")
    for data in board1:
        for char in data:
            board.append(char)
    board1.close()
    return board

#Static estimate at the Opening position - White
def openingStaticEstimate(boardSt):
    noOfWhite = 0
    noOfBlack = 0
    staticEstimate = 0
    for i in range(0,len(boardSt)):
        if(boardSt[i]=='W'):
            noOfWhite= noOfWhite+1
        
        elif(boardSt[i]=='B'):
            noOfBlack = noOfBlack+1

    staticEstimate = noOfWhite-noOfBlack 
    return staticEstimate

   
def MiniMax(depth,gameBoard,flag):
    out = BoardLogic.output_Class()
    inp = BoardLogic.output_Class()
    boardList = list()
    if(depth==0):
        total_Count_final = openingStaticEstimate(gameBoard)
        out = BoardLogic.output_Class(total_Count_final,out.count+1,gameBoard)
        return out
    
    if(flag==1):
        boardList = BoardLogic.gen_Move_Opening(gameBoard)
        out.value = minimum_Value
    
    else:
        boardList = BoardLogic.gen_MoveOpening_Black(gameBoard)
        out.value = maximum_Value
        
    for bposition in boardList:
        if(flag==1):
            inp = MiniMax(depth-1,bposition,0)
            if(inp.value>out.value):
                out.value=inp.value
                out.boardState = bposition
            out.count = out.count + inp.count
            
        else:
            inp = MiniMax(depth-1,bposition,1)
            if(inp.value<out.value):
                out.value=inp.value
                out.boardState = bposition
            out.count = out.count + inp.count
            
    return out
            
board = get_Board_State()  
output = MiniMax(depth,board,1)
print("Input position",''.join(get_Board_State()))
write_Board_State(output.boardState)
print("Output Position:", ''.join(output_State()))
print("Position evaluated by static estimation:",output.count)
print("MINIMAX esitmate:",output.value)

  
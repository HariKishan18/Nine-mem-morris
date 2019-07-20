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
    for line in board1:
        for char in line:
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
    for line in board1:
        for char in line:
            board.append(char)
    board1.close()
    return board

#Improved Static estimate at the Opening position - White
def openingStaticEstimate_Improved(boardSt):
    noOfWhite = 0
    noOfBlack = 0
    for i in range(0,len(boardSt)):
        if(boardSt[i]=='W'):
            noOfWhite= noOfWhite+1
        
        elif(boardSt[i]=='B'):
            noOfBlack = noOfBlack+1
    mills_count = 0
    staticEstimate = 0
    difference = 0
    difference = noOfWhite-noOfBlack 
    for each in range(0,len(boardSt)):
        if(boardSt[each]=='x'):
            if(BoardLogic.checkMills(each,boardSt,"W")==True):
                mills_count = mills_count+1
    staticEstimate = mills_count+difference
    return staticEstimate

def MiniMaxImproved(depth,gameBoard,flag):
    out = BoardLogic.output_Class()
    inp = BoardLogic.output_Class()
    boardList = list()
    if(depth==0):
        total_Count_final = openingStaticEstimate_Improved(gameBoard)
        out = BoardLogic.output_Class(total_Count_final,out.count+1,gameBoard)
        return out
    
    if(flag==1):
        boardList = BoardLogic.gen_Move_Opening(gameBoard)
        out.value = minimum_Value
    
    else:
        boardList = BoardLogic.gen_MoveOpening_Black(gameBoard)
        out.value = maximum_Value
        
    for bpos in boardList:
        if(flag==1):
            inp = MiniMaxImproved(depth-1,bpos,0)
            if(inp.value>out.value):
                out.value=inp.value
                out.boardState = bpos
            out.count = out.count + inp.count
            
        else:
            inp = MiniMaxImproved(depth-1,bpos,1)
            if(inp.value<out.value):
                out.value=inp.value
                out.boardState = bpos
            out.count = out.count + inp.count
            
    return out
            
board = get_Board_State()  
out = MiniMaxImproved(depth,board,1)
print("Input position",''.join(get_Board_State()))
write_Board_State(out.boardState)  
print("Output Position:", ''.join(output_State()))
print("Position evaluated by static estimation:",out.count)
print("MINIMAX esitmate:",out.value)

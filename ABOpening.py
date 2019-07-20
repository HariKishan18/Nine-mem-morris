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
        for ch in line:
            board.append(ch)
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
        for ch in line:
            board.append(ch)
    board1.close()
    return board


#Static estimate at the Opening position - White
def openingStaticEstimate(boardSt):
    noOfWhite = 0
    noOfBlack = 0
    staticEstimate = 0
    for posi in range(0,len(boardSt)):
        if(boardSt[posi]=='W'):
            noOfWhite= noOfWhite+1
        
        elif(boardSt[posi]=='B'):
            noOfBlack = noOfBlack+1

    staticEstimate = noOfWhite-noOfBlack 
    return staticEstimate

def ABOpening(depth,board,alpha,beta,flag):
    inp = BoardLogic.output_Class()
    out = BoardLogic.output_Class()
    boardPositionList = list()
    total_Count_final = 0
    if(depth==0):
        total_Count_final = openingStaticEstimate(board)
        out.value = total_Count_final
        out.count = out.count +1
        return out
    
    if(flag==1):
        boardPositionList = BoardLogic.gen_Move_Opening(board)

    else:
        boardPositionList = BoardLogic.gen_MoveOpening_Black(board)
       
    for bposition in boardPositionList:
        if(flag==1):
            inp = ABOpening(depth-1,bposition,alpha,beta, 0)
            if (inp.value > alpha):
                alpha = inp.value
                out.boardState = bposition
            out.count = out.count + inp.count
        else:
             inp = ABOpening(depth-1,bposition,alpha,beta, 1)
             if (inp.value < beta):
                beta = inp.value
                out.boardState = bposition
             out.count = out.count + inp.count
        if(alpha>=beta):
            break
    if (flag==1):
        out.value =alpha
    else:
        out.value = beta
    return out

   
board = get_Board_State()
output = ABOpening(depth,board,minimum_Value,maximum_Value,1)

print("Input position",''.join(get_Board_State()))
write_Board_State(output.boardState)
print("Output Position:", ''.join(output_State()))
print("Positions evaluated by static estimation:",output.count)
print("AB Estimate:",output.value)


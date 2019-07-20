import sys
import BoardLogic

maxValue = sys.maxsize
minValue = -sys.maxsize
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


def ABGame(depth,board,alpha,beta,flag):
    inp = BoardLogic.output_Class()
    out = BoardLogic.output_Class()
    
    if(depth==0):
        noOfwhite = 0
        noOfBlack = 0
        total_Count_final = 0
        for i in range(0,len(board)):
            if(board[i]=="W"):
                noOfwhite = noOfwhite+1
            if(board[i]=="B"):
                noOfBlack = noOfBlack+1
        total_Count_final = noOfwhite-noOfBlack
        midgame_List = BoardLogic.generateMovesMidgameEndgameBlack(board)
        midgame_listsize = len(midgame_List)
        if(noOfBlack<=2):
            out.value = 10000
        elif(noOfwhite<=2):
            out.value = -10000
        elif(midgame_listsize==0):
            out.value = 10000
        else:
            out.value = 1000*(total_Count_final)-midgame_listsize
        out.count = out.count+1
        out.boardState = board 
        return out
    
    moves_List = list()
    if(flag==1):    
        moves_List = BoardLogic.generateMovesMidgameEndgame(board)
        
    else:
        moves_List = BoardLogic.generateMovesMidgameEndgameBlack(board)
            
    for bPos in moves_List:
        if(flag==1):
            inp = ABGame(depth-1,bPos,alpha,beta,0)
            if(inp.value> alpha):
                alpha = inp.value
                out.boardState = bPos
            out.count = out.count + inp.count
        else:
            inp = ABGame(depth-1,bPos,alpha,beta,1)
            if(inp.value< beta):
                beta = inp.value
                out.boardState = bPos
            out.count = out.count + inp.count
        if(alpha>=beta):
            break
        
    if (flag==1):
        out.value = alpha
    else:
        out.value = beta
    return out

board = get_Board_State()
out = ABGame(depth,board,minValue,maxValue,1)

print("Input i",''.join(get_Board_State()))
write_Board_State(out.boardState)
print("Output i:", ''.join(output_State()))
print("positions evaluated by static estimation:",out.count)
print("AB estimate:",out.value)

#ask for input size
#display board
#ask for input
#display inital board
#apply algo
#if not goal and platue
    #ask for forward states
#if not goal but local minima
    #display local minima error
#else if goal stop
from random import random
local_bfs_mode=False
plateu_mode=False
n=None
def disboard(state):
    for i in range(n-1):
    #print("|",state[0],"|",state[1],"|",state[2],"|",state[3],"|")
        print(" |", state[i],end="")
    print(" |")
def compute_heuristic(board):
    #number of queens under attack
    global n
    heuristic_value=0
    for col_i in range(0,n-1):
        for col_j in range(col_i+1,n-1):
            #same row
            #print(col_i,col_j)
            if board[col_i]==board[col_j]:
                heuristic_value+=1
            #diagonal
            diag=col_j-col_i
            if (board[col_i]==board[col_j]+diag) | (board[col_i]==board[col_j]-diag) :
                heuristic_value+=1
    return heuristic_value

def apply_simple_HillClimbing(actual_board):
    global n,local_bfs_mode,plateu_mode
    board=actual_board
    while True:

        Current_heuristic=compute_heuristic(board)
        sol=board
        print(sol)
        tCurrent_heuristic=Current_heuristic
        prev_heuristic=Current_heuristic
        possible_candidate=None
        print("curr",Current_heuristic)
        if compute_heuristic(sol)==0: #if works
            return sol                 #if works

        for x in range(n-1):
            temp=board.copy()
            for y in range(n - 1):
                if board[x] == 1 + y:
                    continue
                #print(y+1)
                temp[x]=1+y
                temp_heuristic=compute_heuristic(temp)
                #print(temp,"::",temp_heuristic,"tc:",tCurrent_heuristic)
                if temp_heuristic<tCurrent_heuristic:
                    possible_candidate=temp.copy()
                    tCurrent_heuristic=temp_heuristic
                
                if local_bfs_mode:
                    pass
                    # enable local maxima mode ie. seach random n childs or run till till you find uppers ie explore all minma
                    # values and consider only front neighbour
                if plateu_mode:
                    temp_heuristic == tCurrent_heuristic
                    possible_candidate = temp.copy()
                    tCurrent_heuristic = temp_heuristic
                    #enable plateu mode in else if prev heuristic is same move to next state with same heuristic till fall
                else:
                    pass
                # or use simulated Annealing


                print(possible_candidate,":",tCurrent_heuristic)

            print("")
        sol = possible_candidate
        if sol== None:
            print("found plateu or local minima prob ")
            return board

        print(sol,"heurstic of sol:",compute_heuristic(sol))
        if (compute_heuristic(sol)==0) or (compute_heuristic(sol)==prev_heuristic):
            return sol
        else:
            board=list(sol.copy())
            print("board changed")
            disboard(board)

def stimulateA(board):
    # Set initial temp
    temp = 1000
    #Cooling rate
    coolingRate = 0.003
    while temp>1:
        pass
        #if neighbour has good probality select it. if has bad then
        # select bad and explore till not bored or temp doesnt fall


def makememain():

    global n,local_bfs_mode,plateu_mode
    input_state=[]
    sudo=input("do you want to access sudo block? y/n")
    if sudo=="y"or sudo=="Y":
        local_bfs_mode=False
        plateu_mode=False

    n = int(input("Enter size of queen problem"))+1
    disboard(list(range(1,n)))
    print("Enter start position")
    for i in range(1, n):
        print("Enter row no for queen", i, ":")
        #only row no as column is fixed for each queen Q1 goes in col 1, Q2 in col 2 so on..
        item = int(input())
        if (item<1) | (item>n):
            print("invalid choice try again..")
            return
        input_state.append(item)
    disboard(input_state)
    disboard(apply_simple_HillClimbing(input_state))
    #apply_simple_HillClimbing(input_state)


makememain()
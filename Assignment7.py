def show():
    for row in Game_board:
        for col in row:
            print(col,end=" ")
         print()

 def game_1():
    if Game_board[0][0] == "o" and Game_board[0][1]=="o" or Game_board[1][0]=="o" and Game_board[1][1]=="o" and Game_board[1][2]=="o" and Game_board[2][0]=="o" and Game_board[2][1]=="o" and Game_board[2][2]=="o" or Game_board[0][0]=="o"and game_board[1][1]=="o"and game_board[2][2]=="o":
        print("player 1 win. ")
        quit()

def game_2():
    if Game_board[0][0]=="x" and Game_board[0][1]=="x" and Game_board[0][2]=="x"and Game_board[1][0]=="x" and Game_board[1][1]=="x" and Game_board[1][2]=="x" or Game_board[2][0]=="x" and Game_board[2][1]=="x"  and Game_board[2][2]=="x":
        print("player 2 win. ")
        quit()



Game_board= [["-","-","-",]
             ["-","-","-"]
             ["-","-","-"]] 
show()

while True:
    #player1 o
    print("player1")
    while True:
        row= int(input("Enter a row: "))
        col= int(input("Enter a col: "))
        if 0<= row <=2 and 0<= col <=2:
            if Game_board[row][col]=="-":
                Game_board[row][col]="o"
                show()
                game_1()
                game_2()
                beark
               else:
                print("yek khoone dige entwkhab kon
            else:
                print(" bein 1 and 2 entekhab kon. ") 

while True:
    #player2
    print("player2")
while True:
    row = int(input("Enter row: "))
    col = int(input("Enter col: "))
    if 0<= row <=2 and 0<= col <=2:
        if Game_board[row][col]=="-":
            Game_board[row][col]=="x":
            show()
            game_2()
            break
        else:
            print("yek khoone dige entekhab kon. ")
        else:
            print("bein 1 and 2 entakhab kon. ")
                          
 
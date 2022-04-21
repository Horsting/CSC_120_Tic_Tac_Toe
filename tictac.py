print("Welcome to tic tac toe")
play = str(input("Press 1 to start"))
board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
if play == "1":
    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])
    while play == "1":
        print("Player 1 Turn")
        print(0, 1, 2)
        print(3, 4, 5)
        print(6, 7, 8)
        p1 = int(input("enter value of board space you wish to place a marker on"))
        while p1 not in range(0, 9):
            print("Space not found")
            p1 = int(input("enter value of board space you wish to place a marker on"))
        if board[p1] != "-":
            print("space taken")
            p1 = int(input("enter value of board space you wish to place a marker on"))
        board[p1] = "X"
        if board[0] == board[1] and board[0] == board[2]:
            if board[0] != "-":
                break
        if board[0] == board[3] and board[0] == board[6]:
            if board[0] != "-":
                break
        if board[0] == board[4] and board[4] == board[8]:
            if board[0] != "-":
                break
        if board[3] == board[1] and board[3] == board[5]:
            if board[3] != "-":
                break
        if board[6] == board[7] and board[6] == board[8]:
            if board[6] != "-":
                break
        if board[1] == board[4] and board[1] == board[7]:
            if board[1] != "-":
                break
        if board[2] == board[5] and board[2] == board[8]:
            if board[2] != "-":
                break
        if board[2] == board[4] and board[2] == board[6]:
            if board[2] != "-":
                break
        print(board[0], board[1], board[2])
        print(board[3], board[4], board[5])
        print(board[6], board[7], board[8])
        print("Player 2 Turn")
        print(0, 1, 2)
        print(3, 4, 5)
        print(6, 7, 8)
        p2 = int(input("enter value of board space you wish to place a marker on"))
        while p2 not in range(0, 9):
            print("Space not found")
            p2 = int(input("enter value of board space you wish to place a marker on"))
        if board[p2] != "-":
            print("space taken")
            p2 = int(input("enter value of board space you wish to place a marker on"))
        board[p2] = "O"
        if board[0] == board[1] and board[0] == board[2]:
            if board[0] != "-":
                break
        if board[0] == board[3] and board[0] == board[6]:
            if board[0] != "-":
                break
        if board[0] == board[4] and board[0] == board[8]:
            if board[0] != "-":
                break
        if board[3] == board[1] and board[3] == board[5]:
            if board[3] != "-":
                break
        if board[6] == board[7] and board[6] == board[8]:
            if board[6] != "-":
                break
        if board[1] == board[4] and board[1] == board[7]:
            if board[1] != "-":
                break
        if board[2] == board[5] and board[2] == board[8]:
            if board[2] != "-":
                break
        if board[2] == board[4] and board[2] == board[6]:
            if board[2] != "-":
                break
        print(board[0], board[1], board[2])
        print(board[3], board[4], board[5])
        print(board[6], board[7], board[8])

    print("Game over")
    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])

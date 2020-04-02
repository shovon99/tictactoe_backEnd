class Board:
    boardData = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    player1Sign = 'X'
    player2Sign = 'O'
    player1History = []
    player2History = []

    Won = False
    P1Won = False
    P2Won = False

    def __init__(self):
        super().__init__()
    
    def getSnapshot(self):
        x = ''
        for i in range(len(self.boardData)):
            for j in range(len(self.boardData[0])):
                x = x + str(self.boardData[i][j])
        return x

    def isDraw(self):
        if (0 not in self.boardData[0]) and (0 not in self.boardData[1]) and (0 not in self.boardData[2])  :
            return True
        return False

    def reset(self):
        self.boardData = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.player1History = []
        self.player2History = []
        self.Won = False
        self.P1Won = False
        self.P2Won = False

    def decodePosition(self, ind):
        if ind == 1:
            return [0, 0]
        elif ind == 2:
            return [0, 1]
        elif ind == 3:
            return [0, 2]
        elif ind == 4:
            return [1, 0]
        elif ind == 5:
            return [1, 1]
        elif ind == 6:
            return [1, 2]
        elif ind == 7:
            return [2, 0]
        elif ind == 8:
            return [2, 1]
        elif ind == 9:
            return [2, 2]

    def win_indexes(self, n):
        for r in range(n):
            yield [(r, c) for c in range(n)]
        # Columns
        for c in range(n):
            yield [(r, c) for r in range(n)]
        # Diagonal top left to bottom right
        yield [(i, i) for i in range(n)]
        # Diagonal top right to bottom left
        yield [(i, n - 1 - i) for i in range(n)]


    def is_winner(self, player):
        n = len(self.boardData)
        for indexes in self.win_indexes(n):
            if all(self.boardData[r][c] == player for r, c in indexes):
                return True
        return False

    def printBoardRaw(self):
        print()
        for i in range(len(self.boardData)):
            for j in range(len(self.boardData[0])):
                print(self.boardData[i][j], end=' ')
            print()
        print()

    def printBoard(self):
        print()
        for i in range(len(self.boardData)):
            for j in range(len(self.boardData[0])):
                if self.boardData[i][j] == 1:
                    print('|', self.player1Sign, '|', end=' ')
                elif self.boardData[i][j] == 2:
                    print('|', self.player2Sign, '|', end=' ')
                else:
                    print('| - |', end=' ')
            print()
            print()
        print()

    def player1Move(self, ind):
        if not self.Won:
            if (ind not in self.player1History) and (ind not in self.player2History):
                self.player1History.append(ind)
                [x, y] = self.decodePosition(ind)
                self.boardData[x][y] = 1

                if(self.is_winner(1)):
                    self.Won = True
                    self.P1Won = True
                    print("Player 1 WINS!")
                if(self.isDraw()):
                    self.Won = True
                return True
            else:
                return False
        else:
            print("Already Won! ")
            return False
    
    def player2Move(self, ind):
        if not self.Won:
            if (ind not in self.player1History) and (ind not in self.player2History):
                self.player2History.append(ind)
                [x, y] = self.decodePosition(ind)
                self.boardData[x][y] = 2
                if(self.is_winner(2)):
                    self.Won = True
                    self.P2Won = True
                    print("Player 2 WINS!")
                if(self.isDraw()):
                    self.Won = True
                return True
            else:
                return False
        else:
            print("Aleary Won!")
            return False


def boardViewer(X):
    boardData = [
        [X[0], X[1], X[2]],
        [X[3], X[4], X[5]],
        [X[6], X[7], X[8]]
    ]

    print()
    for i in range( len(boardData)):
        for j in range(len(boardData[0])):
            if boardData[i][j] == "1":
                print('|', "X", '|', end=' ')
            elif boardData[i][j] == "2":
                print('|', "O", '|', end=' ')
            else:
                print('| - |', end=' ')
        print()
        print()
    print()
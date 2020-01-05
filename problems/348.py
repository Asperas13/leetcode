class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.board = [0 for _ in range(2 * n + 2)]
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        score = 1 if player == 1 else -1

        self.board[row] += score
        if self.board[row] in (self.n, -self.n):
            return player

        self.board[self.n + col] += score
        if self.board[self.n + col] in (self.n, -self.n):
            return player

        if row == col:
            self.board[-2] += score
            if self.board[-2] in (self.n, -self.n):
                return player

        if self.n - 1 - row == col:
            self.board[-1] += score
            if self.board[-1] in (self.n, -self.n):
                return player

        return 0
# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        capture = 0
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    for dy, dx in directions:
                        y, x = i, j
                        while 0 <= y < 8 and 0 <= x < 8:
                            if board[y][x] == 'p':
                                capture += 1
                                break
                            if board[y][x] == 'B':
                                break

                            y += dy
                            x += dx
                    break

        return capture
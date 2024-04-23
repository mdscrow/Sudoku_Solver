class Solution:

    def solveSudoku(self, board: List[List[str]]) -> None:
        self.board = board
        rC = self.rowCheck(0)
        cC = self.columnCheck(2)

        print(f'Row Check: {rC}\nColumn Check: {cC}')
    
    def rowCheck(self,rowIndex):
        possibility = list("123456789")
        row = self.board[rowIndex]
        for value in row:
            if value != ".":
                possibility.remove(value)
        return possibility

    def columnCheck(self,columnIndex):
        possibility = list("123456789")
        for row in self.board:
            if row[columnIndex] != ".":
                possibility.remove(row[columnIndex])
        return possibility

    def squareCheck(self,squareX, squareY):
        pass


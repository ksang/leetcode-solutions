BOARD = [
    ['5','3','.','.','7','.','.','.','.'],
    ['6','.','.','1','9','5','.','.','.'],
    ['.','9','8','.','.','.','.','6','.'],
    ['8','.','.','.','6','.','.','.','3'],
    ['4','.','.','8','.','3','.','.','1'],
    ['7','.','.','.','2','.','.','.','6'],
    ['.','6','.','.','.','.','2','8','.'],
    ['.','.','.','4','1','9','.','.','5'],
    ['.','.','.','.','8','.','7','7','9']
]

class Solution:
    # @param {character[][]} board
    # @return {boolean}
    def isValidSudoku(self, board):
        ct = {}
        if len(board) != 9: return False
        for row, table in enumerate(board):
            if len(table) != 9:
                return False
            for col, item in enumerate(table):
                if item != '.':
                    for i in range(0,row):
                        if ct.get((i,col)) == item:
                            return False
                    for j in range(0,col):
                        if ct.get((row,j)) == item:
                            return False
                    ct[(row,col)] = item
        return True

        

if __name__ == '__main__':
    print Solution().isValidSudoku(BOARD)
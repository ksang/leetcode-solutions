BOARD = [
            "..5.....6",
            "....14...",
            ".........",
            ".....92..",
            "5....2...",
            ".......3.",
            "...54....",
            "3.....42.",
            "...27.6.."
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
                    for i in range(row/3*3,row):
                        for j in range(col/3*3,col/3*3+3):
                            #print "i:%s, j:%s, row:%s, col:%s " % (i,j,row,col)
                            if ct.get((i,j)) == item:
                                #print 'sub box check failed'
                                return False
                    ct[(row,col)] = item
        return True

if __name__ == '__main__':
    print Solution().isValidSudoku(BOARD)
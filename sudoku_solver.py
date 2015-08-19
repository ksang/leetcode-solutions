BOARD = [
            [".",".","5",".",".",".",".",".","6"],
            [".",".",".",".","1","4",".",".","."],
            [".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".","9","2",".","."],
            ["5",".",".",".",".","2",".",".","."],
            [".",".",".",".",".",".",".","3","."],
            [".",".",".","5","4",".",".",".","."],
            ["3",".",".",".",".",".","4","2","."],
            [".",".",".","2","7",".","6",".","."]
        ]

class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.

    def solveSudoku(self, board):
        val = self.PossibleVals(board) # dict {(i,j):[possible values]}
        self.Solver(board,val)

    def PossibleVals(self, board):
        num = "123456789"
        val = {}
        # init d, d is used for memoize what value already used in this row/col/subbox
        d = {(i/3,j/3):[] for i in xrange(9) for j in xrange(9)}
        d.update({("row", i):[] for i in xrange(9)})
        d.update({("col", j):[] for j in xrange(9)})

        for i in xrange(9):
            for j in xrange(9):
                ele = board[i][j]
                if ele != ".":
                    d[("row", i)].append(ele)
                    d[("col", j)].append(ele)
                    d[(i/3, j/3)].append(ele)
                else:
                    # only the '.' element needs to be solved
                    val[(i,j)]=[]
        # puts possible values in val{}, excluding which we have in d{}
        for (i,j) in val.keys():
            val[(i,j)] = [n for n in num if (   n not in d[("row",i)]
                                                and n not in d[("col",j)]
                                                and n not in d[(i/3,j/3)]
                                                )
                        ]
        return val

    def Solver(self, board, val):
        if len(val) == 0:
            return True
        # get key has least possibilities (least length)
        mkey = min(val.keys(), key = lambda x: len(val[x]))
        nums = val[mkey]
        for n in nums:
            (i,j) = mkey
            board[i][j] = n
            # save the element that will update its possibilites for undo
            update = {mkey: val[mkey]}
            del val[mkey]
            valid = True
            for ind in val.keys():
                if n in val[ind]:
                    # if the current processing value will exclude possibilty of other elements
                    if ind[0] == i or ind[1] == j or (ind[0]/3,ind[1]/3) == (i/3,j/3):
                        update[ind] = n
                        val[ind].remove(n)
                        if len(val[ind]) == 0:
                            valid = False
                            break
            # recursively call Solver to process element has least possibilities in DFS manner
            # when the first element possiblities are solved, all the other should also be solved.
            if valid and self.Solver(board,val):
                return True
            else:
                board[i][j] = "."
                val = self.undo(update,val)
        return False

    def undo(self, update, val): # add what we deleted back
        for k in update:
            if k not in val:
                val[k] = update[k]
            else:
                val[k].append(update[k])
        return val

if __name__ == '__main__':
    b = BOARD
    Solution().solveSudoku(b)
    for r in b: print r
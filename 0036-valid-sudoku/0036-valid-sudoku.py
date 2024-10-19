class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        tempSetRow= set()
        tempSetCol=set()
        boxSets = [[set() for _ in range(3)] for _ in range(3)] 
        for i in range(9):
            tempSetRow.clear()
            tempSetCol.clear()
            for j in range(9):
                if board[i][j] != '.':
                    if int(board[i][j]) >= 1 and int(board[i][j]) <= 9:
                        if board[i][j]  not in tempSetRow:
                            tempSetRow.add(board[i][j])
                        else:
                            return False
                    else:
                        return False
                    

                if board[j][i] != '.':
                    if int(board[j][i]) >= 1 and int(board[j][i]) <= 9:
                        if board[j][i]  not in tempSetCol:
                            tempSetCol.add(board[j][i])
                        else:
                            return False
                    else:
                        return False
                
                boxRow = i // 3
                boxCol = j // 3
                if board[i][j] != '.':
                    if board[i][j] in boxSets[boxRow][boxCol]:
                        return False
                    boxSets[boxRow][boxCol].add(board[i][j])

            
        return True
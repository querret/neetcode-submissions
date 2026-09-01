from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        boxs = defaultdict(set)

        for r, row in enumerate(board):
            for c, value in enumerate(row):
                box_id = (r // 3, c // 3)

                if value != ".":
                    if value in columns[c]:
                        return False
                    else: 
                        columns[c].add(value)
                
                    if value in rows[r]:
                        return False
                    else: 
                        rows[r].add(value)

                    if value in boxs[box_id]:
                        return False
                    else:
                        boxs[box_id].add(value)
        return True
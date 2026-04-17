from collections import defaultdict
from typing import List, Dict
import time

ROW_SIZE = 9
COLUMN_SIZE = 9

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = defaultdict(set)
        column_set = defaultdict(set)
        subgrid_set = defaultdict(set)

        for r in range(ROW_SIZE):
            for c in range(COLUMN_SIZE):
                cell = board[r][c]
                subgrid_index = ((r // 3) * 3) + (c // 3)

                if cell == ".":
                    continue
                
                if (
                    cell in row_set[r]
                    or cell in column_set[c]
                    or cell in subgrid_set[subgrid_index]
                ):
                    return False
                
                row_set[r].add(cell)
                column_set[c].add(cell)
                subgrid_set[subgrid_index].add(cell)

        return True
        
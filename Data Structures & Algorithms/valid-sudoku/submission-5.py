from collections import defaultdict
from typing import List, Dict
import time

ROW_SIZE = 9
COLUMN_SIZE = 9

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = defaultdict(set)
        col_set = defaultdict(set)
        subgrid_set = defaultdict(set)

        for row in range(ROW_SIZE):
            for col in range(COLUMN_SIZE):
                subgrid_index = ((row // 3) * 3) + (col // 3)
                cell = board[row][col]
                if cell == ".":
                    continue

                if (
                    cell in row_set[row] or
                    cell in col_set[col] or
                    cell in subgrid_set[subgrid_index]
                ):
                    return False

                row_set[row].add(cell)
                col_set[col].add(cell)
                subgrid_set[subgrid_index].add(cell)
        
        return True
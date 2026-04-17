from collections import defaultdict
from typing import List, Dict
import time

ROW_SIZE = 9
COLUMN_SIZE = 9

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        subgrid_map = defaultdict(list)

        for r in range(COLUMN_SIZE):
            if not self.is_valid_row(board, r):
                return False
            elif not self.is_valid_column(board, r):
                return False
            
            for c in range(ROW_SIZE):
                cell = board[r][c]
                grid_index = self.find_subgrid_index(r, c)
                subgrid_map[grid_index].append(cell)

        if not self.is_valid_subgrid(subgrid_map):
            return False

        return True

    def find_subgrid_index(self, row: str, column: str) -> int:
        return ((row // 3) * 3) + (column // 3)

    def contains_duplicate(self, list: List[str]) -> bool:
        duplicate = {}

        for num in list:
                if num != '.' and num in duplicate:
                    return True
                duplicate[num] = True

        return False

    def is_valid_row(self, board: List[List[str]], r_index: int) -> bool:
        if self.contains_duplicate(board[r_index]):
            return False

        return True

    def is_valid_column(self, board: List[List[str]], r_index: int) -> bool:
        column = ['.'] * COLUMN_SIZE

        for c_index in range(COLUMN_SIZE):
            column[c_index] = board[c_index][r_index]

        if self.contains_duplicate(column):
            return False
        
        return True

    def is_valid_subgrid(self, subgrid: Dict[str, List[int]]) -> bool:
        for subgrid_items in subgrid.values():
            if self.contains_duplicate(subgrid_items):
                return False
            
        return True
        
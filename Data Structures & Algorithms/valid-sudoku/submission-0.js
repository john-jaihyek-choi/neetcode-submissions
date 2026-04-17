class Solution {
    /**
     * @param {character[][]} board
     * @return {boolean}
     */
    isValidSudoku(board) {
        const rowMap = new Map();
        const columnMap = new Map();
        const squareMap = new Map();

        for(let row = 0; row < board.length; row++) {
            for(let column = 0; column < board.length; column++) {
                const cell = board[row][column];
                const squareIndicies = Math.floor(row/3) * 3 + Math.floor(column/3);

                if(cell === '.') {
                    continue;
                }

                if(
                    rowMap.get(row)?.has(cell) ||
                    columnMap.get(column)?.has(cell) ||
                    squareMap.get(squareIndicies)?.has(cell)
                ) {
                    return false;
                }

                rowMap.set(row, new Set(rowMap.get(row)).add(cell));
                columnMap.set(column, new Set(columnMap.get(column)).add(cell));
                squareMap.set(squareIndicies, new Set(squareMap.get(squareIndicies)).add(cell));
            }
        }

        return true;
    }
}

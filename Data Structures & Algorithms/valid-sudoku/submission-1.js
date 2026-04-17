class Solution {
    /**
     * @param {character[][]} board
     * @return {boolean}
     */
    // isValidSudoku(board) {
    //     const rowMap = new Map();
    //     const columnMap = new Map();
    //     const squareMap = new Map();

    //     for(let row = 0; row < board.length; row++) {
    //         for(let column = 0; column < board.length; column++) {
    //             const cell = board[row][column];
    //             const subSquareIndex = Math.floor(row/3) * 3 + Math.floor(column/3);

    //             if(cell === '.') {
    //                 continue;
    //             }

    //             if(
    //                 rowMap.get(row)?.has(cell) ||
    //                 columnMap.get(column)?.has(cell) ||
    //                 squareMap.get(subSquareIndex)?.has(cell)
    //             ) {
    //                 console.log(`rowMap`, rowMap)
    //                 console.log(`columnMap`, columnMap)
    //                 console.log(`squareMap`, squareMap)
                    
    //                 return false;
    //             }

    //             rowMap.set(row, new Set(rowMap.get(row)).add(cell));
    //             columnMap.set(column, new Set(columnMap.get(column)).add(cell));
    //             squareMap.set(subSquareIndex, new Set(squareMap.get(subSquareIndex)).add(cell));
    //         }
    //     }

    //     console.log(`rowMap - ${rowMap}`)
    //     console.log(`columnMap - ${columnMap}`)
    //     console.log(`squareMap - ${squareMap}`)

    //     return true;
    // }

    isValidSudoku(board) {
        const rowMap = new Map();
        const columnMap = new Map();
        const subgridMap = new Map();

        for (let x = 0; x < board.length; x++) {
            for (let y = 0; y < board[x].length; y++) {
                const cell = board[x][y];
                const subgridIndex = (Math.floor(x/3) * 3) + Math.floor(y/3);

                if(cell === ".") {
                    continue;
                }

                if(
                    rowMap.get(x)?.has(cell) ||
                    columnMap.get(y)?.has(cell) ||
                    subgridMap.get(subgridIndex)?.has(cell)
                ) {
                    return false;
                }

                rowMap.set(x, new Set(rowMap.get(x)).add(cell));
                columnMap.set(y, new Set(columnMap.get(y)).add(cell));
                subgridMap.set(subgridIndex, new Set(subgridMap.get(subgridIndex)).add(cell));
            }
        }

        return true;
    }
}

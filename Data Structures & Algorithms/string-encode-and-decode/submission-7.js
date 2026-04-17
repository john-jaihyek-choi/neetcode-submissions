class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        // // solution 1
        // const encodedStr = strs.map(str => {
        //     return this.utfEncode(str);
        // })

        // console.log(encodedStr);

        // return encodedStr;

        // solution 2
        let encodedStr = ''
        for (const str of strs) {
            const strLength = str.length;

            encodedStr += `${strLength}#${str}`;
        }

        console.log(encodedStr);

        return encodedStr;
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        // // solution 1
        // const decodedStr = str.map(str => {
        //     return this.utfDecode(str);
        // })

        // return decodedStr;

        // solution 2
        const decodedArr = [];
        let i = 0;

        while (i < str.length) {
            let j = i;
            while(str[j] !== '#') {
                j++;
            }
            let length = parseInt(str.substring(i, j), 10);
            i = j + 1;
            j = i + length;
            decodedArr.push(str.substring(i, j));
            i = j;
        }

        return decodedArr;
    }

    // utfEncode(str) {
    //     return str.split('').map(char => {
    //         const code = char.codePointAt(0);
    //         const shift = 5;
    //         const shiftedChar = ((code + shift) % 0x10FFFF)

    //         return String.fromCodePoint(shiftedChar);
    //     }).join('')
    // }

    // utfDecode(str) {
    //     return str.split('').map(char => {
    //         const code = char.codePointAt(0);
    //         const shift = 5;
    //         const shiftedChar = ((code - shift) % 0x10FFFF) % 0x10FFFF;
            
    //         return String.fromCodePoint(shiftedChar);
    //     }).join('')
    // }
}

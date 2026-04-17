class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        // 1. iterate strs value
        // 2. for every strs[i], designate a code, base, and a shift value
            // if strs[i] is not an alphabet, don't encode the character
        // 3. apply a logic that shifts the value
            // make sure that the value wraps around within lower and uppercase alphabet
        // 4. return the shifted value
        // 5. join the shifted value


        const encodedStr = strs.map(str => {
            return this.utfEncode(str);
        })

        console.log(encodedStr);

        return encodedStr;
    }

    utfEncode(str) {
        return str.split('').map(char => {
            const code = char.codePointAt(0);
            const shift = 5;
            const shiftedChar = ((code + shift) % 0x10FFFF)

            return String.fromCodePoint(shiftedChar);
        }).join('')
    }

    utfDecode(str) {
        return str.split('').map(char => {
            const code = char.codePointAt(0);
            const shift = 5;
            const shiftedChar = ((code - shift) % 0x10FFFF) % 0x10FFFF;
            
            return String.fromCodePoint(shiftedChar);
        }).join('')
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        // 1. iterate strs value
        // 2. for every strs[i], designate a code, base, and a shift value
            // if strs[i] is not an alphabet, don't decode the character
        // 3. apply a logic that shifts the value
            // make sure that the value wraps around within lower and uppercase alphabet
        // 4. return the shifted value
        // 5. join the shifted value

        const decodedStr = str.map(str => {
            return this.utfDecode(str);
        })

        console.log(decodedStr);

        return decodedStr;
    }
}

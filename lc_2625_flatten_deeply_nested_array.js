/**
 * @param {any[]} arr
 * @param n {number}
 * @return {any[]}
 */
let flat = function (arr, n) {
    let res = [];
    const flattening = (nums, l) => {
        for(const num of nums){
            if(Array.isArray(num) && l > 0){
                flattening(num, l - 1);
            } else {
                res.push(num);
            }
        }
    }
    flattening(arr, n);
    return res;
};

// Example 1:
// Input:
let arr = [1, [2, [3, 4]]];
// Output:
// [1, 2, [3, 4]]
console.log(flat(arr, 1));
if (JSON.stringify(flat(arr, 1)) !== JSON.stringify([1, 2, [3, 4]])) {
    throw new Error("Failed test case 1");
} else {
    console.log("Test case 1 passed");
}

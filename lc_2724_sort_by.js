/**
 * @param {Array} arr
 * @param {Function} fn
 * @return {Array}
 */
let sortBy = function (arr, fn) {
    return arr.sort((a, b) => fn(a) - fn(b))
};

// How to use:
arr = [{"x": 1}, {"x": 0}, {"x": -1}]
sortBy(arr, o => o.x)
console.log(arr) // [{"x": -1}, {"x": 0}, {"x": 1}]


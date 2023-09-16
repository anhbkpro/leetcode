/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
let join = function(arr1, arr2) {
    const combinedArr = [...arr1, ...arr2]
    const merged = {}

    combinedArr.forEach((item) => {
        const id = item.id
        if(merged[id]){
            merged[id] = {...merged[id], ...item}
        } else {
            merged[id] = item
        }
    });

    const joinedArr = Object.values(merged);
    joinedArr.sort((a, b) => a.id - b.id);

    return joinedArr;
};

// Example 1:
// Input:
let arr1 = [
    {"id": 1, "x": 1},
    {"id": 2, "x": 9}
];
let arr2 = [
    {"id": 3, "x": 5}
];
// Output:
// [{"id": 1, "x": 1}, {"id": 2, "x": 9}, {"id": 3, "x": 5}]
console.log(join(arr1, arr2));

arr1 = [
    {"id": 1, "x": 2, "y": 3},
    {"id": 2, "x": 3, "y": 6}
];
arr2 = [
    {"id": 2, "x": 10, "y": 20},
    {"id": 3, "x": 0, "y": 0}
];
// Output:
// [{"id": 1, "x": 2, "y": 3}, {"id": 2, "x": 10, "y": 20}, {"id": 3, "x": 0, "y": 0}]
console.log(join(arr1, arr2));
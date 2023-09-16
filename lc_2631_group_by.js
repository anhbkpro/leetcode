Array.prototype.groupBy = function(fn){
    return this.reduce((acc, item) => {
        const key = fn(item);
        if(!acc[key]){
            acc[key] = [];
        }
        acc[key].push(item);
        return acc;
    }, {});
}


// Example 1:
// Input:
let arr = [
    {"id": 1, "x": 1},
    {"id": 1, "x": 1},
    {"id": 2, "x": 9}
];
// Output:
// {
//     "1": [{"id": 1, "x": 1}, {"id": 1, "x": 1}],
//     "2": [{"id": 2, "x": 9}]
// }
console.log(arr.groupBy(o => o.id));

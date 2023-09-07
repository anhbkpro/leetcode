/**
 * @param {Function} fn
 * @return {Function}
 */
var once = function(fn) {
  let hasBeenCalled = false;
  return function(...args){
    if (!hasBeenCalled) {
      hasBeenCalled = true;
      return fn(...args);
    }
  }
};

let fn = (a,b,c) => (a + b + c)
let onceFn = once(fn)

console.log(onceFn(1,2,3)); // 6
console.log(onceFn(2,3,6)); // returns `undefined` without calling fn

// How to test:
// 1. Run this file with `node lc_2666_allow_one_function_call_per_time_unit.js`
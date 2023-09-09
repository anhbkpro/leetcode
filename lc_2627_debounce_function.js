/**
 * @param {Function} fn
 * @param {number} t milliseconds
 * @return {Function}
 */
const debounce = function(fn, t) {
    let interval;
    return function(...args) {
        const lastCall = Date.now();
        clearInterval(interval);
        interval = setInterval(() => {
            if (Date.now() - lastCall >= t) {
                clearInterval(interval);
                fn(...args);
            }
        }, 1);
    }
};

/**
 * const log = debounce(console.log, 100);
 * log('Hello'); // cancelled
 * log('Hello'); // cancelled
 * log('Hello'); // Logged at t=100ms
 */

const log = debounce(console.log, 100);
log('Hello'); // cancelled
log('Hello'); // cancelled
log('Hello'); // Logged at t=100ms

// How to test:
// 1. Run this file with `node lc_2627_debounce_function.js`
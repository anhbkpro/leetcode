var TimeLimitedCache = function() {
    this.cache = {};
};

/**
 * @param {number} key
 * @param {number} value
 * @param {number} duration until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    let exists = false;
    if (this.cache[key]) {
        exists = true;
    }
    this.cache[key] = {
        value: value,
        expires: Date.now() + duration
    };
    return exists;
};

/**
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
    if (this.cache[key]) {
        if (this.cache[key].expires > Date.now()) {
            return this.cache[key].value;
        } else {
            delete this.cache[key];
        }
    }
    return -1;
};

/**
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
    let count = 0;
    Object.keys(this.cache).forEach(function(key) {
        if (this.cache[key].expires > Date.now()) {
            count++;
        } else {
            delete this.cache[key];
        }
    }, this);
    return count;
};

/**
 * Your TimeLimitedCache object will be instantiated and called as such:
 * var obj = new TimeLimitedCache()
 * obj.set(1, 42, 1000); // false
 * obj.get(1) // 42
 * obj.count() // 1
 */

const obj = new TimeLimitedCache();
console.log(obj.set(1, 42, 1000)); // false
console.log(obj.get(1)); // 42
console.log(obj.count()); // 1

// How to test:
// 1. Run this file with `node lc_2622_cache_with_time_limit.js`

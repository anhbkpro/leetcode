const promiseAll = async function (functions) {
    return new Promise((resolve, reject) => {
        if (functions.length === []) {
            resolve([])
            return
        }

        const res = new Array(functions.length).fill(null)

        let resolvedCount = 0

        functions.forEach(async (el, idx) => {
            try {
                res[idx] = await el()
                resolvedCount++
                if (resolvedCount === functions.length) {
                    resolve(res)
                }
            } catch (err) {
                reject(err)
            }
        })
    })
};

console.log('==promiseAll: Implementation 1: Using async/await Syntax')
const promise = promiseAll([() => new Promise(res => res(42))]);
promise.then(console.log); // [42]

const promiseAllV2 = function (functions) {
    return new Promise((resolve, reject) => {
        if (functions.length === []) {
            resolve([])
            return
        }

        const res = new Array(functions.length).fill(null)

        let resolvedCount = 0

        functions.forEach((el, idx) => {
            el().then((subResult) => {
                res[idx] = subResult
                resolvedCount++
                if (resolvedCount === functions.length) {
                    resolve(res)
                }
            }).catch((err) => {
                reject(err)
            })
        })
    })
};

console.log('==promiseAllV2: Implementation 2: Using then/catch Syntax')
const promise2 = promiseAllV2([() => new Promise(res => res(42))]);
promise2.then(console.log); // [42]

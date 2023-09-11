var promiseAll = async function(functions) {
    return new Promise((resolve,reject) => {
        if(functions.length === []) {
            resolve([])
            return
        }

        const res = new Array(functions.length).fill(null)

        let resolvedCount = 0

        functions.forEach(async (el,idx) => {
            try {
                res[idx] = await el()
                resolvedCount++
                if(resolvedCount=== functions.length) {
                    resolve(res)
                }
            } catch(err) {
                reject(err)
            }
        })
    })
};

const promise = promiseAll([() => new Promise(res => res(42))]);
promise.then(console.log); // [42]

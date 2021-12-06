const fs = require('fs')
const data = fs.readFileSync('../inputs/day6_mike.txt', {encoding: 'utf8', flag: 'r'})
const array = data.split(',').map(num => parseInt(num))

// so slow...

function lantern(array, days) {
    for (let i = 0; i < days; i++) {
       for (let j = 0; j < array.length; j++) {
            if (array[j] === 0) {
                array.push(9)
                array[j] = 6
            } else {
                array[j] -= 1
            }
        } 
    }
    return array.length
    
}

// more poo poo, but functional

function totalLanterns(array, days) {

    let hash = {
        '0':0,
        '1':0,
        '2':0,
        '3':0,
        '4':0,
        '5':0,
        '6':0,
        '7':0,
        '8':0,
        '9':0
    }

    for (let i = 0; i < array.length; i++) {
       hash[array[i]] ? hash[array[i]] += 1 : hash[array[i]] = 1
    }

    for (let i = 0; i < days; i++) {
       for (let j = 0; j <= 9; j++) { 
            if (j === 0) {
                hash[7] += hash[0]
                hash[9] += hash[0]
                hash[0] = 0
            } else {
                hash[j-1] += hash[j]
                hash[j] -= hash[j]
            }
        }
    }

    return Object.values(hash).reduce((a,b) => a + b)

}

console.log(totalLanterns(array, 256))

// increasing depth
const fs = require('fs')
const data = fs.readFileSync('../inputs/day1_mike.txt', {encoding: 'utf8', flag: 'r'})
const array = data.split('\n').map(num => parseInt(num))

function increasingDepth(depths) {
    let count = 0
    for (let i = 1; i < depths.length; i++) {
        if (depths[i-1] < depths[i]) {
            count+=1
        }
    }
    return count
}

console.log(increasingDepth(array)) 


function increasingDepthWindow(depths) {
    let count = 0
    for (let i = 1; i < depths.length-2; i++) {
        sumPrevious = depths[i-1] + depths[i] + depths[i+1]
        sumCurrent = depths[i] + depths[i+1] + depths[i+2]
        if (sumCurrent > sumPrevious) {
            count+=1
        }
    }
    return count
}

console.log(increasingDepthWindow(array)) 

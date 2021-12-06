const fs = require('fs')
const data = fs.readFileSync('../inputs/day3/day3_mike.txt', {encoding: 'utf8', flag: 'r'})
const array = data.split('\n')

function binDiagnostic(bits) {
    let oneCount = 0
    let zeroCount = 0
    let gammaArray = []
    let epsilonArray = []


    for (let i = 0; i < bits[0].length; i++) {
        for (let j = 0; j < bits.length; j++) {
            
            if (parseInt(bits[j][i]) === 1) {
                oneCount += 1
            } else {
                zeroCount += 1
            }

        }
        if (oneCount > zeroCount) {
            gammaArray.push(1)
        } else {
            gammaArray.push(0)
        }

        oneCount = 0
        zeroCount = 0

    }

    gammaArray.forEach(bit => {
        if (bit === 1) {
            epsilonArray.push(0)
        } else {
            epsilonArray.push(1)
        }
    });
    gamma = parseInt(gammaArray.join(''),2)
    epsilon = parseInt(epsilonArray.join(''),2)

    return gamma*epsilon

}

console.log(binDiagnostic(array))


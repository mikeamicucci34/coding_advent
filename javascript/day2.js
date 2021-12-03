const fs = require('fs')
const data = fs.readFileSync('../inputs/day2/day2_mike.txt', {encoding: 'utf8', flag: 'r'})
const array = data.split('\n')

function subCorse(corse) {
    let horizontal = 0
    let depth = 0

    for (let i = 0; i < corse.length; i++) {
        splitArr = corse[i].split(" ");
        action = splitArr[0]

        int = parseInt(splitArr[1])

        switch(action) {
            case "forward":
                horizontal+=int;
                break
            case "down":
                depth+=int;
                break
            case "up":
                depth-=int;
                break
        }
    }
    return horizontal*depth
}

console.log(subCorse(array))


function subCorseAim(corse) {
    let horizontal = 0
    let depth = 0
    let aim = 0

    for (let i = 0; i < corse.length; i++) {
        splitArr = corse[i].split(" ");
        action = splitArr[0]

        int = parseInt(splitArr[1])

        switch(action) {
            case "forward":
                horizontal+=int;
                depth+=aim*int
                break
            case "down":
                aim+=int;
                break
            case "up":
                aim-=int
                break
        }
    }
    return horizontal*depth
}

console.log(subCorseAim(array))
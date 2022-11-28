import fs from "node:fs/promises"

let data = JSON.parse(await fs.readFile("./tsconfig.json","utf-8"))
data.compilerOptions.watch = false
console.log(data)

await fs.writeFile("./tsconfig.json",JSON.stringify(data))

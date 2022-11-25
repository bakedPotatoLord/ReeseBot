import * as dotenv from 'dotenv' // see https://github.com/motdotla/dotenv#how-do-i-use-dotenv-with-import
dotenv.config()
export {disses} from "./assets/disses.js"  ; 

export const TOKEN = process.env["TOKEN"]
export const CLIENTID = process.env["CLIENTID"]

export const guildIds:string[] = [
  "986808066353815595"
]








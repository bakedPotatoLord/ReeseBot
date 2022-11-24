import * as dotenv from 'dotenv' // see https://github.com/motdotla/dotenv#how-do-i-use-dotenv-with-import
dotenv.config()

export {disses} from "./assets/disses.js"  ; 

function getToken():string{
  if(process.env.TOKEN){
    return process.env.TOKEN
  }else{
    throw new Error("no token in the env file")
  }
}
const TOKEN =getToken()

export const clientIds:string[] = [
  "986808066353815595"
]

export {TOKEN}







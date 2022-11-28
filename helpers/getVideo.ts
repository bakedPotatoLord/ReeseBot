import fetch from "node-fetch"
import {RAPIDAPIKEY} from "../consts.js"

export async function getYoutubeVideo(url:string){
  
  if(RAPIDAPIKEY){
    let encodedUrl = `https://youtube-to-mp4.p.rapidapi.com/url=&title?url=${encodeURIComponent(url)}`;

    let options = {
      method: 'GET',
      headers: {
        'X-RapidAPI-Key': RAPIDAPIKEY,
        'X-RapidAPI-Host': 'youtube-to-mp4.p.rapidapi.com'
      }
    };

    fetch(encodedUrl, options)
      .then(res => res.json())
      .then(json => console.log(json))
      .catch(err => console.error('error:' + err));
  }
}

getYoutubeVideo("https://www.youtube.com/shorts/Zmx0Ou5TNJs")


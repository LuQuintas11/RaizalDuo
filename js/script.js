fetch("https://youtube.googleapis.com/youtube/v3/search?part=snippet&channelId=UCmAnQ_N8P76uVbrRhrT-1OQ&key=AIzaSyATSs9N3idzOJvK9hMG1X2-4oAZ1LF8iD4")
.then((result)=>{
    return result.json()

}).then((data)=>{
   console.log(data)
   let videos=data.items
   let videosContainer = document.querySelector(".youtube-content")
   let videosLink=document.querySelector(".youtube-link")
   
   for(video of videos){
    videosContainer.innerHTML +=`
       <img  class="img" src="${video.snippet.thumbnails.default.url}"></img>`

        videosLink.innerHTML += 
      ` <a href ="https://www.youtube.com/playlist?list=${video.id.playlistId}"></a>`


    console.log(video.id.playlistId) 

        
        
   }
   
})
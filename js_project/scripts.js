let storyListSec = document.getElementById('story-list');

window.onload = async function (){
    let response = await fetch('http://127.0.0.1:8000/api/stories/')
    let storyList = await response.json();
    console.log(storyList);
    for (let story of storyList){
        storyListSec.innerHTML += `<div class="col-md-4">
        <div class="card" >
            <img src="${story.image}" class="card-img-top" alt="...">
            <div class="card-body">
              <h5 class="card-title">${story.title}</h5>
              <p class="card-text">${story.description}</p>
              <button onclick="goDetailPage('${story.slug}')" href="http://localhost:8000/en/stories/${story.slug}/" class="btn btn-primary">Go somewhere</button>
            </div>
          </div>
    </div>`
    }
}

async function goDetailPage(storySlug){
    let response = await fetch(`http://127.0.0.1:8000/api/stories/${storySlug}/`)
    let story = await response.json();
    document.getElementById('page-content').innerHTML = `
            <div class="card mb-3">
        <img src="${story.image}" class="card-img-top" alt="...">
        <div class="card-body">
            <h5 class="card-title">${story.title}</h5>
            <p class="card-text">${story.description}</p>
            <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p>
        </div>
        </div>
    `
}
const urlParams = new URLSearchParams(window.location.search);
const myParam = urlParams.get('id');
console.log(myParam)

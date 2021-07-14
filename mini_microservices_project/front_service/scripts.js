let postList = document.getElementById("post-list");

async function renderPost(post){
    let comments = await getComments(post.id);
    postList.innerHTML+=`<div class="col-md-3">
    <div class="card p-4">
        <h3 class="card-title">${post.title}</h3>
        <div class="card-body">
            <form action="" method="post">
                <div class="form-group">
                    <label for="">Content</label>
                    <input type="text" class="form-control">
                </div>
                <input type="submit" value="Create Comment">
            </form>
            <ul>
                ${ comments.map(comment => `<li>${comment.content}</li>`).join('') }
            </ul>
        </div>
    </div>
</div>`
}

async function getComments(postId){
    let res = await fetch(`http://localhost:5001/posts/${postId}/comments/`);
    return  await res.json();
}

document.getElementById('create-post')
.addEventListener('submit', async function(e){
    e.preventDefault();
    let postData = {
        'title': this.title.value
    }
    console.log(postData);

    let res = await fetch('http://localhost:5000/posts', {
        method: 'POST',
        headers:{
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(postData)
    });
    if (res.ok){
        let post = await res.json()
        renderPost(post);
        alert('yaradildi');
    }else{
        alert('sehvlik bas verdi');
    }

})

async function getPosts(){
    let res = await fetch('http://localhost:5000/posts');
    let data = await res.json();
    for (let post of data){
        console.log(post)
        renderPost(post);
    }
}

window.onload = () => {
    getPosts();

}
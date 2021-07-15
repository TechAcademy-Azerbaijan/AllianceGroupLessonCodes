let postList = document.getElementById("post-list");

async function renderPost(post){
    let comments = post.comments || [];
    postList.innerHTML+=`<div class="col-md-3">
    <div class="card p-4">
        <h3 class="card-title">${post.title}</h3>
        <div class="card-body">
            <form class="create-comment" data-postid=${post.id} method="post">
                <div class="form-group">
                    <label for="">Content</label>
                    <input type="text" name="content" class="form-control">
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

async function createComment(form){
    console.log(form);
    let postId = form.dataset.postid;
    let commentData = {
        'content': form.content.value
    }
    console.log(commentData);

    let res = await fetch(`http://localhost:5001/posts/${postId}/comments/`, {
        method: 'POST',
        headers:{
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(commentData)
    });
    if (res.ok){
        let comment = await res.json();
        console.log(comment);
        let ul = form.parentElement.getElementsByTagName('ul')[0];
        ul.innerHTML += `<li>${comment.content}</li>`

        alert('yaradildi');
    }else{
        alert('sehvlik bas verdi');
    }

}

window.addEventListener('submit', async function(e){
    e.preventDefault();
    if (e.target.classList.contains('create-comment')){
        await createComment(form=e.target)
    }
})

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
    let res = await fetch('http://localhost:5003/posts');
    let data = await res.json();
    for (let post of data){
        console.log(post)
        renderPost(post);
    }
}

window.onload = () => {
    getPosts();

}
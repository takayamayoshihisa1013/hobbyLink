function toggleLike(postId) {
    const csrfToken = document.querySelector(`#like-form-${postId} [name=csrfmiddlewaretoken]`).value;
    
    fetch(`/hobbyLink/toggle_like/${postId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
        },
        body: JSON.stringify({}),
    })
    .then(response => {
        if (!response.ok) {
            return response.json().then(data => { throw new Error(data.error || 'Network response was not ok'); });
        }
        return response.json();
    })
    .then(data => {
        if (data.success) {
            document.querySelector(`#like-count-${postId}`).innerText = data.like_count;
            const likeIcon = document.querySelector(`#like-icon-${postId}`);
            if (data.liked) {
                likeIcon.classList.add('liked');
            } else {
                likeIcon.classList.remove('liked');
            }
        } else {
            alert(`Error toggling like: ${data.error}`);
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}


function comment(event, postId) {
    event.preventDefault();
    window.location.href = `/hobbyLink/timeline/comment/${postId}/`;
}
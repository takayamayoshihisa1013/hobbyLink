function getPostId(postId) {
    var click_i = postId.split("-")[1];
    const posts = document.querySelectorAll(".post_img");
    posts.forEach(element => {
        // すべての画像divを非表示に設定
        element.style.display = "none";
    });
    // クリックされたポストに対応する画像divだけを表示
    var targetElement = document.getElementById(`post_img-${click_i}`);
    if (targetElement) {
        targetElement.style.display = "block";
    }
}

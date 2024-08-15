window.addEventListener("scroll", function() {
    var user_post = document.querySelector(".user_post");
    var img_list = document.querySelector('.img_list');
    var post_list = this.document.querySelector(".post_list");
    var user_post_top = user_post.getBoundingClientRect().top;

    if (user_post_top <= 0) {
        img_list.style.position = "fixed";
        img_list.style.top = 0;
        img_list.style.width = "38.9%";
        img_list.style.left = "58%";
        post_list.style.marginRight = "50%";
    } else {
        img_list.style.position = "static";
        img_list.style.width = "50%";
        img_list.style.left = 0;
        post_list.style.marginRight = 0;
    }
})

document.getElementById("user_search").addEventListener("input", function() {
    console.log("aaaaaaaaaaaaaaaaa")
    document.querySelectorAll(".suggestion-item").forEach(user => {
        user.addEventListener("click", function() {

            console.log(this.id, "aaaaa");
        })
    })
})
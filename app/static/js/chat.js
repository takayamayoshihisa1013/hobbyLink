document.querySelectorAll(".friend_name").forEach(chat => {
    
    chat.addEventListener("click", function() {
        let chat_number = this.id.split("-")[1];
        console.log(chat_number)
        document.querySelectorAll(".chat").forEach(chat_num => {
            chat_num.style.display = "none";
            console.log(chat_num.style.display);
        });
        document.querySelector(".friend_search").style.display = "none";
        let targetChatBody = document.getElementById(`chat_body-${chat_number}`);
        if (targetChatBody) {
            console.log(targetChatBody)
            targetChatBody.style.display = "block";
        }

        document.querySelectorAll(".chat").forEach(chat_num => {
            // chat_num.style.display = "none";
            console.log(chat_num.style.display);
        });
    });
});

document.getElementById("new_chat").addEventListener("click", function() {
    document.querySelectorAll(".chat").forEach(chat_num => {
        chat_num.style.display = "none";
        console.log(chat_num.style.display);
    });

    document.querySelector(".friend_search").style.display = "block";
}) 
    




            // 既存のイベントリスナーを削除してから追加
            // let sendButton = document.getElementById("send");
            // sendButton.replaceWith(sendButton.cloneNode(true));
            // sendButton = document.getElementById("send");

            // sendButton.addEventListener("click", function() {
            //     let send_text = document.getElementById("send_text").value;
            //     let send_image = document.getElementById("send_image").files[0];

            //     let formData = new FormData();
            //     formData.append("text", send_text);
            //     if (send_image) {
            //         formData.append("image", send_image);
            //     }

            //     let csrfToken = document.getElementById("csrf_token").value;
            //     fetch(`${chat_number}/`, {
            //         method: "POST",
            //         headers: {
            //             'X-CSRFToken': csrfToken,
            //         },
            //         body: formData
            //     })
            //     .then(response => response.json())
            //     .then(data => {
            //         if (data) {
            //             let newMessageDiv = document.createElement("div");
            //             newMessageDiv.className = data.sender_id == data.login_id ? 'my' : '';

            //             if (data.image_url) {
            //                 let user_name = document.createElement("h3");
            //                 user_name.innerHTML = data.sender;
            //                 let p = document.createElement("p");
            //                 let span = document.createElement("span");
            //                 span.classList.add("text");
            //                 span.innerHTML = data.text;
            //                 p.appendChild(span);
            //                 let chat_img = document.createElement("img");
            //                 chat_img.setAttribute("src", `/static/images${data.image_url}`);
            //                 newMessageDiv.appendChild(user_name);
            //                 newMessageDiv.appendChild(p);
            //                 newMessageDiv.appendChild(chat_img);
            //             } else {
            //                 let user_name = document.createElement("h3");
            //                 user_name.innerHTML = data.sender;
            //                 let p = document.createElement("p");
            //                 let span = document.createElement("span");
            //                 span.classList.add("text");
            //                 span.innerHTML = data.text;
            //                 p.appendChild(span);
            //                 newMessageDiv.appendChild(user_name);
            //                 newMessageDiv.appendChild(p);
            //             }
            //             targetChatBody.appendChild(newMessageDiv);

            //             document.getElementById("send_text").value = '';
            //             document.getElementById("send_image").value = "";
            //         }
            //     })
            //     .catch(error => console.error('エラーが発生しました:', error));
            // });

            // document.getElementById("send_text").addEventListener("keypress", function(event) {
            //     if (event.key === "Enter") {
            //         event.preventDefault();
            //         sendButton.click();
            //     }
            // });
        // }
    

document.getElementById("new_chat").addEventListener("click", function() {
    document.querySelector(".chat").style.display = "none";
    document.querySelector(".friend_search").style.display = "block";

})


document.querySelectorAll(".friend_name").forEach(chat => {
    chat.addEventListener("click", function() {
        console.log(this.id.split("-"));
        let chat_number = this.id.split("-")[1];

        document.querySelectorAll(".chat_body").forEach(chat_num => {
            chat_num.style.display = "none";
        });

        let targetChatBody = document.getElementById(`chat_body-${chat_number}`);
        if (targetChatBody) {
            targetChatBody.style.display = "block";
            // 既存のイベントリスナーを削除してから新しいものを追加
            let sendButton = document.getElementById("send");
            let newSendButton = sendButton.cloneNode(true); // クローンを作成
            sendButton.parentNode.replaceChild(newSendButton, sendButton); // 古いボタンを新しいものに置き換えするらしい

            newSendButton.addEventListener("click", function() {
                let send_text = document.getElementById("send_text").value;
                console.log(send_text);
                fetch(`${chat_number}/?q=${send_text}`)
                .then(response => response.json())
                .then(data => {
                    if (data) {
                        let newMessageDiv = document.createElement("div");
                        newMessageDiv.className = data.sender_id == data.login_id ? 'my' : '';
                        newMessageDiv.innerHTML = `
                        <h3>${data.sender}</h3>
                        <p><span class="text">${data.text}</span></p>
                        `;
                        targetChatBody.appendChild(newMessageDiv);
                        document.getElementById("send_text").value = '';
                    }

                })
            })
            // エンターキーでメッセージを送信するリスナーを追加
            document.getElementById("send_text").addEventListener("keypress", function(event) {
                if (event.key === "Enter") {
                    event.preventDefault();  // デフォルトのエンターキー動作をキャンセル
                    newSendButton.click();  // 送信ボタンをクリック
                }
            });
        }
    })
})


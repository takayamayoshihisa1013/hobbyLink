// CSRFトークンを取得する関数を定義
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

document.getElementById("user_search").addEventListener("input", function() {   
    // 入力した文字を読み取ってる 
    const query = this.value;

    console.log(query);

    if (query.length > 2) {
        // search_usersページに飛んで処理をもらう
        fetch(`search_users/?q=${query}`)
        .then(response => response.json())
        .then(data => {

            const suggestionsDiv = document.getElementById("suggestions");
            suggestionsDiv.innerHTML = "";

            console.log(data);

            data.forEach(user => {
                const suggestionItem = document.createElement("div");
                suggestionItem.className = "suggestion-item";
                suggestionItem.innerHTML = user.user_name;
                suggestionItem.id = user.user_id;

                // サジェスト項目をクリックしたときの処理
                suggestionItem.addEventListener("click", function() {
                    document.getElementById("user_search").value = user.user_name;
                    console.log(this.id);
                    suggestionsDiv.innerHTML = ""; // サジェストをクリア
                    
                    fetch(`create_table/?q=${this.id}`, {
                        "method":"POST",
                        "headers":{
                            'Content-Type': 'application/json', // JSON形式で送信することを示す
                            'X-CSRFToken': getCookie('csrftoken') 
                        }
                    })
                    .then(response => {
                        if (response.ok) {
                            window.location.reload()
                        } else {
                            console.error('POSTリクエストが失敗しました:', response.statusText);
                        }
                    })
                });
                suggestionsDiv.appendChild(suggestionItem);
            });
        })
    } else {
        document.getElementById("suggestions").innerHTML = "";
    }
})
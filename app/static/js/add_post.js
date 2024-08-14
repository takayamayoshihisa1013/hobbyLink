console.log("a")

document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("add_img").addEventListener("click", function () {
        var add_input = document.createElement("input");
        add_input.type = "file";
        add_input.name = "post_images";
        document.querySelector(".img_file").appendChild(add_input);
    });



    const tagInput = document.getElementById('tag_input');
    const suggestionsBox = document.getElementById('suggestions');
    fetch("/hobbyLink/tag_list/")
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        console.log(data);
        const options = data.map(item => item.name);

        tagInput.addEventListener('input', function () {
            const value = tagInput.value.trim();
            if (value.endsWith('#')) {
                showSuggestions('');
            } else if (value.endsWith(' ')) {
                tagInput.value += '#';
                showSuggestions('');
            } else {
                showSuggestions(value.split(' ').pop());
            }
        });

        function showSuggestions(input) {
            suggestionsBox.innerHTML = '';
            const filteredOptions = options.filter(option => option.includes(input));
            filteredOptions.forEach(option => {
                const suggestionItem = document.createElement('div');
                suggestionItem.classList.add('suggestion-item');
                suggestionItem.textContent = option;
                suggestionItem.addEventListener('click', () => {
                    tagInput.value = tagInput.value.replace(/[^ ]*$/, '') + option + ' ';
                    suggestionsBox.innerHTML = '';
                    tagInput.focus();
                });
                suggestionsBox.appendChild(suggestionItem);
            });
        }
    })  

    document.addEventListener('click', function (event) {
        if (!tagInput.contains(event.target) && !suggestionsBox.contains(event.target)) {
            suggestionsBox.innerHTML = '';
        }
    });


    //     var textarea = new InputSuggest('textarea');
    // // var input    = new InputSuggest('input');
    // textarea.setSuggestions(['AirMac Express', 'Apple TV', 'Apple Watch', 'Mac Book Pro', 'Mac Book', 'iMac', 'iPad', 'iPad mini', 'iPhone', 'iPod', 'iPod Touch']);

    //     function addTagRow() {
    //     const post_tag = document.querySelector(".post_tag");

    //     // 新しいtag_rowを作成
    //     var tag_row = document.createElement("div");
    //     tag_row.classList.add("tag_row");

    //     // ひとつ前の.add_tagを削除
    //     var prev_add_tag = document.querySelector(".add_tag");
    //     if (prev_add_tag) {
    //         prev_add_tag.remove();
    //     }

    //     // 新しいタグ入力欄を3つ追加
    //     for (var i = 0; i < 3; i++) {
    //         var tag = document.createElement("div");
    //         tag.classList.add("tag");

    //         var tag_input = document.createElement("input");
    //         tag_input.setAttribute("list", "tag");
    //         tag_input.setAttribute("placeholder", "タグ");

    //         var tag_datalist = document.createElement("datalist");
    //         tag_datalist.id = "tag";

    //         var tag_option = document.createElement("option");
    //         tag_option.value = "#おっはー";
    //         tag_datalist.appendChild(tag_option);

    //         tag.appendChild(tag_input);
    //         tag.appendChild(tag_datalist);
    //         tag_row.appendChild(tag);
    //     }

    //     // 新しいadd_tagを作成
    //     var add_tag = document.createElement("div");
    //     add_tag.classList.add("add_tag");

    //     var add_tag_button = document.createElement("button");
    //     add_tag_button.id = "add_tag";
    //     add_tag_button.textContent = "+";
    //     add_tag.appendChild(add_tag_button);

    //     tag_row.appendChild(add_tag);
    //     post_tag.appendChild(tag_row);

    //     // 新しいadd_tagボタンにイベントリスナーを追加
    //     add_tag_button.addEventListener("click", addTagRow);
    // }

    // // 初期のadd_tagボタンにイベントリスナーを追加
    // document.getElementById("add_tag").addEventListener("click", addTagRow);

})



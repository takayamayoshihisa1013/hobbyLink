console.log("aaaaaa")

function previewImage(event) {
    var file = event.target.files[0];
    var reader = new FileReader();

    reader.onload = function(){
        // console.log("s")
        const upload_img = document.querySelector(".img img");
        if (upload_img == null){
            var preview = document.createElement('img');
            preview.src = reader.result;
            preview.alt = 'User Icon';

            var fileLabel = document.getElementById('file-label');
            fileLabel.innerHTML = ''; // アイコンを削除
            fileLabel.appendChild(preview); // 画像を追加
        } else {
            upload_img.src = reader.result;
        }
    };

    if (file) {
        reader.readAsDataURL(file);
    }
}
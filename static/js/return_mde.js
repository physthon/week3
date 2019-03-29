function getData() {
    let xml = new XMLHttpRequest();
    xml.open("GET", "http://localhost:2000/list-mde",false)
    xml.send()
    console.log(xml.responseText);
    return xml.responseText;
}

function getRealData(){
    let obj_x = JSON.parse(getData());
    let value = obj_x.value;
    console.log(value);
    return value;
}

var simplemde = new SimpleMDE({
    element: document.getElementById("return_mde"),
    previewRender: function (plainText, preview) {
        setTimeout(function () {
            markjax(plainText, preview);
        }, 50);
        return preview.innerHTML;
    }
});

simplemde.value(getRealData())
simplemde.togglePreview();
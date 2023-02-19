function getDocLoc(name) {
    console.log("running")
    fetch("local/"+name+".json").then(resp => resp.json()).then(data => {
        document.getElementById("text_entry").value = data.text;
        document.getElementById("doc_name_text").innerHTML = "Doc name: "+data.name;
        document.getElementById("text_entry").style.color = "#"+data.colour;
        document.getElementById("text_entry").style.fontSize = data.font_size;
    })
}
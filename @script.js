function fontButton() {
    console.log("Font button clicked");
}

function underlineButton() {
    console.log("Underline button clicked");
}

function titleButton() {
    console.log("Title button clicked");
}

function headingButton() {
    document.getElementById("headings_top").style.display = "block";
    setInterval(function() {
        document.getElementById("headings_top").style.display = "none";
    }, 4000)
}

function boldButton() {
    console.log("Bold button clicked");
}

function italicsButton() {
    let preText = document.getElementById("document").elements.namedItem("text_entry").value.substring(0, document.getElementById("document").elements.namedItem("text_entry").value.selectionStart-1);
    let selectedText = document.getElementById("document").elements.namedItem("text_entry").value.substring(document.getElementById("document").elements.namedItem("text_entry").value.selectionStart, document.getElementById("document").elements.namedItem("text_entry").value.selectionEnd).italics();
    let postText = document.getElementById("document").elements.namedItem("text_entry").value.substring(document.getElementById("document").elements.namedItem("text_entry").value.selectionEnd+1, document.getElementById("document").elements.namedItem("text_entry").value.length)
    document.getElementById("text_entry").innerHTML = preText + selectedText + postText;
}

function newPageButton() {
    console.log("New page button clicked");
    let temp = data_template;
    temp.name = prompt("File name: ");
    temp.text = document.getElementById("text_entry").value;
    files.push(temp)
}

function toDoButton() {
    console.log("To do button clicked");
}

function recent1() {
    getDocLoc("test")
}

function recent2() {
    getDocLoc("Document")
}

function recent3() {
    getDocLoc("How to view this")
}
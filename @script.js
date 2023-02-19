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
    console.log("Heading button clicked");
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
    document.getElementById("doc_name_text").innerHTML = "Doc name: "+prompt("File name");
}

function toDoButton() {
    console.log("To do button clciked");
}
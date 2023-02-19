const data_template = {
    "name": null,
    "text": null
}
const files = [
    {
        "name": "test",
        "text": "This is a test document."
    }
]

addEventListener('submit', (e) => {
    let data = {
        "name": document.getElementById("doc_name_text").innerHTML.replace("Doc name: ", ""),
        "text": document.getElementById("document").elements.namedItem("text_entry").value
    }
    console.log(data);
});

addEventListener('load', (e) => {
    document.getElementById("doc_name_text").innerHTML = "Doc name: ";
    document.getElementById("headings_top").style.animation = "none";
    document.getElementById("headings_top").style.display = "none";
});
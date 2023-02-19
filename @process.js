addEventListener('submit', (e) => {
    let data = document.getElementById("document").elements.namedItem("text_entry").value;
    let name = doc
});
addEventListener('load', (e) => {
    document.getElementById("doc_name_text").innerHTML = "Doc name: ";
    document.getElementById("headings_top").style.animation = "disappear 0.5s smooth";
});
document.addEventListener('click', (e) => {
    if (document.getElementById("headings_top").contains(e.target) == false) {
        document.getElementById("headings_top").style.animation = "disappear 0.5s smooth";
        console.log("1")
    } else {
        document.getElementById("headings_top").style.animation = "appear 0.5s smooth";
        console.log("2")
    }
})
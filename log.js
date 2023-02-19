const switchers = [...document.querySelectorAll(".switcher")];

switchers.forEach((item) => {
	console.log(item.className);
  item.addEventListener("click", function () {
    switchers.forEach((item) =>
      item.parentElement.classList.remove("is-active")
    );
    this.parentElement.classList.add("is-active");
  });
});


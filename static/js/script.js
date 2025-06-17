document.querySelectorAll(".modal-trigger").forEach((btn) => {
  btn.addEventListener("click", () =>
    document.body.classList.add("modal-open")
  );
});

document.querySelectorAll(".modal-close").forEach((btn) => {
  btn.addEventListener("click", () =>
    document.body.classList.remove("modal-open")
  );
});

document.addEventListener("keydown", (e) => {
  if (e.key === "Escape") {
    document.body.classList.remove("modal-open");
    window.location.hash = "";
  }
});

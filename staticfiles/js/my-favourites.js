let selectedFavouriteFormId = null;

const removeFavouriteButtons = document.getElementsByClassName(
  "btn-remove-favourite",
);
const removeFavouriteConfirmButton = document.getElementById(
  "removeFavouriteConfirm",
);

for (let button of removeFavouriteButtons) {
  button.addEventListener("click", (e) => {
    selectedFavouriteFormId = e.target.getAttribute("data-form-id");
  });
}

removeFavouriteConfirmButton.addEventListener("click", () => {
  if (selectedFavouriteFormId) {
    const selectedForm = document.getElementById(selectedFavouriteFormId);
    if (selectedForm) {
      selectedForm.submit();
    }
  }
});

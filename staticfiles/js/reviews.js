const editButtons = document.getElementsByClassName("edit-btn");
const reviewText = document.getElementById("id_content");
const reviewForm = document.getElementById("reviewForm");
const submitButton = document.getElementById("submitButton");
const reviewRating = document.getElementById("id_rating");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("delete-btn");
const deleteConfirm = document.getElementById("deleteConfirm");

for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let reviewId = e.currentTarget.getAttribute("data-review-id");
    let reviewContent = document
      .getElementById(`reviewContent${reviewId}`)
      .innerText.trim();
    reviewText.value = reviewContent;
    let reviewRatingNum = document
      .getElementById(`reviewRating${reviewId}`)
      .getAttribute("data-rating");
    reviewRating.value = reviewRatingNum;
    submitButton.innerText = "Update";
    reviewForm.setAttribute("action", `edit_review/${reviewId}`);
  });
}

for (let button of deleteButtons) {
  button.addEventListener("click", (e) => {
    let reviewId = e.currentTarget.getAttribute("data-review-id");
    deleteConfirm.href = `delete_review/${reviewId}`;
    deleteModal.show();
  });
}

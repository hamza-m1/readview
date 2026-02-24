const editButtons = document.getElementsByClassName("btn-edit");
const reviewText = document.getElementById("id_content");
// const reviewRating = document.getElementById("id_rating");
const reviewForm = document.getElementById("reviewForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    console.log("in the edit button event listener");
    let reviewId = e.target.getAttribute("review_id");
    // let reviewRating = document
    //   .getElementById(`reviewRating${reviewId}`)
    //   .getAttribute("rating");
    // console.log(reviewRating);
    console.log(document.getElementById(`reviewContent${reviewId}`));
    let reviewContent = document
      .getElementById(`reviewContent${reviewId}`)
      .innerText.trim();
    // console.log(reviewContent);
    // reviewRating.value = reviewRating;
    // console.log(`reviewRating: ${reviewRating}`);
    reviewText.value = reviewContent;
    submitButton.innerText = "Update";
    reviewForm.setAttribute("action", `edit_review/${reviewId}`);
  });
}

for (let button of deleteButtons) {
  button.addEventListener("click", (e) => {
    let reviewId = e.target.getAttribute("review_id");
    deleteConfirm.href = `delete_review/${reviewId}`;
    deleteModal.show();
  });
}

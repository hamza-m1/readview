const editButtons = document.getElementsByClassName("btn-edit");
const reviewText = document.getElementById("id_content");
// const reviewRating = document.getElementById("id_rating");
const reviewForm = document.getElementById("reviewForm");
const submitButton = document.getElementById("submitButton");

for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let reviewId = e.target.getAttribute("review_id");
    // let reviewRating = document
    //   .getElementById(`reviewRating${reviewId}`)
    //   .getAttribute("rating");
    // console.log(reviewRating);
    let reviewContent = document.getElementById(`reviewContent${reviewId}`)
      .childNodes[1].textContent;
    console.log(reviewContent);
    // reviewRating.value = reviewRating;
    // console.log(`reviewRating: ${reviewRating}`);
    reviewText.value = reviewContent;
    submitButton.innerText = "Update";
    reviewForm.setAttribute("action", `edit_review/${reviewId}`);
  });
}

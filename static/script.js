// Function to toggle sections
function toggleSection(id) {
    var section = document.getElementById(id);
    section.classList.toggle("active");
}

// Function to open the image popup
function openPopup(img) {
    var popup = document.getElementById("imagePopup");
    var popupImg = document.getElementById("popupImg");

    popup.style.display = "flex"; // Show the popup
    popupImg.src = img.src; // Set the clicked image as the popup image
}

// Function to close the image popup
function closePopup() {
    document.getElementById("imagePopup").style.display = "none";
}

// Close popup when clicking outside the image
window.onclick = function(event) {
    var popup = document.getElementById("imagePopup");
    if (event.target === popup) {
        popup.style.display = "none";
    }
};

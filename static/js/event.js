const deleteButton = document.getElementById("delete-button")
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));

deleteButton.addEventListener("click", ()=>{
    deleteModal.show();
});
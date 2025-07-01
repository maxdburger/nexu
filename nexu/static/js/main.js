

document.addEventListener('DOMContentLoaded', function(){
    const openButton = document.getElementById('open-modal-button');
    const closeButton = document.getElementById('close-modal-button');
    const modal = document.getElementById('create-subject-modal')

    if (!openButton || !closeButton || !modal) return;

    openButton.addEventListener('click', function(){
        modal.style.display = 'block';
    })

    closeButton.addEventListener('click', function(){
        modal.style.display = 'none';
    })

    window.addEventListener('click', function(event){
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    })
})
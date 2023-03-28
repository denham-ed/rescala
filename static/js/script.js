$(document).ready(function () {


    // Initialize tool tips
    $(function () {
        $('[data-toggle="tooltip"]').tooltip()
    })

    // Remove Messages
    setTimeout(function(){
        let messages = document.getElementById("msg");
        let alert = new bootstrap.Alert(messages);
        alert.close()
    },3000)


    // https://api.jquery.com/data/
    //Update Goal Inputs
    //Hide Buttons On Load
    //Toggle Buttons
    $(".edit-goal-button").click(function (){
        const goalId = $(this).data('goal-id');
        $(`.edit-goal-range[data-goal-id="${goalId}"]`).toggle()
        $(`.goal-progress[data-goal-id="${goalId}"]`).toggle()
        $(`.save-goal-button[data-goal-id="${goalId}"]`).toggle()
        $(`.delete-goal-button[data-goal-id="${goalId}"]`).toggle()
        $(this).toggle()
    })

    $(".save-goal-button").click(function (){
        const goalId = $(this).data('goal-id');
        $(`.edit-goal-range[data-goal-id="${goalId}"]`).toggle()
        $(`.spinner-border[data-goal-id="${goalId}"]`).show()
        $(this).toggle()
    })

    $(".delete-goal-button").click(function (){
        const goalId = $(this).data('goal-id');
        $(`.edit-goal-button[data-goal-id="${goalId}"]`).toggle()
        $(`.revert-goal-button[data-goal-id="${goalId}"]`).toggle()
        $(`.confirm-delete-button[data-goal-id="${goalId}"]`).toggle()
        $(this).toggle()
    })

    $(".revert-goal-button").click(function (){
        const goalId = $(this).data('goal-id');
        $(`.edit-goal-button[data-goal-id="${goalId}"]`).toggle()
        $(`.delete-goal-button[data-goal-id="${goalId}"]`).toggle()
        $(`.confirm-delete-button[data-goal-id="${goalId}"]`).toggle()
        $(this).toggle()
    })
});



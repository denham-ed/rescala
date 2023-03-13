$(document).ready(function () {
    console.log('ready')


    // Initialize tool tips
    $(function () {
        $('[data-toggle="tooltip"]').tooltip()
    })


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
        // Toggle Buttons to Original State
        const goalId = $(this).data('goal-id');
        $(`.edit-goal-range[data-goal-id="${goalId}"]`).toggle()
        $(`.goal-progress[data-goal-id="${goalId}"]`).toggle()
        $(`.edit-goal-button[data-goal-id="${goalId}"]`).toggle()
        $(`.delete-goal-button[data-goal-id="${goalId}"]`).toggle()
        $(this).toggle()
    })
});



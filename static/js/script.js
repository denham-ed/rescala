$(document).ready(function () {
    console.log('ready')

    // Thanks Chat GPT for making less verbose
    // Add labels to goals on Log screen
    $('[id^="goal-"]').change(function () {
        const goalId = $(this).attr('id').split('-')[1];
        $(`#complete-${goalId}`).text(`${$(this).val()}%`);
    });

    // Initialize tool tips
    $(function () {
        $('[data-toggle="tooltip"]').tooltip()
    })


    // https://api.jquery.com/data/
    //Update Goal Inputs
    $(".edit-goal-range").hide("fast")
    $(".edit-goal-button").click(function (){
        const goalId = $(this).data('goal-id');
        $(`.edit-goal-range[data-goal-id="${goalId}"]`).toggle()
        $(`.goal-progress[data-goal-id="${goalId}"]`).toggle()
    })

});



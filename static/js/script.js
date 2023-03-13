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


    //Update Goal Inputs
    $("#edit-goal-input-1").hide()
    $("#edit-goal-1").click(function (){
        $("#edit-goal-input-1").toggle()
        $("#progress-goal-1").toggle()
    })

});



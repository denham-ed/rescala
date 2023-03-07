// $( document ).ready(function() {
//     console.log('ready')
//     let sessions = $('#sessions-context').data('sessions')
//     return console.log(sessions)
//     console.log(Array.from(sessions))
// });



// Thanks Chat GPT for making less verbose
// Add labels to goals on Log screen

$('[id^="goal-"]').change(function() {
    const goalId = $(this).attr('id').split('-')[1];
    $(`#complete-${goalId}`).text(`${$(this).val()}%`);
});


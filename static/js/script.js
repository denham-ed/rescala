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


    //Chart JS
    const ctx = document.getElementById('myChart');

    new Chart(ctx, {
      type: 'pie',
      data: {
        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
        datasets: [{
          label: '# of Votes',
          data: [12, 19, 3, 5, 2, 3],
          borderWidth: 1
        }]
      },
      options: {
        scales: {
          y: {
            beginAtZero: true
          }
        }
      }
    });



});
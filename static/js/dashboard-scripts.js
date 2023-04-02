const addChart = () => {
    /**
     * Generates a chart to display the distribution of foci in recorded practice sessions
     * Receives focus element on the Dashboard page which contains a JSON list of objects.
     */
    const focus_list = JSON.parse(document.getElementById('focus').textContent);
    if (!focus_list.length) {
        $("#no-chart").html("<p><em>Log a practice</em> to start tracking where you are putting your focus.</p>");
    } else {
        try {
            let ctx = document.getElementById('focus-chart').getContext('2d');
            new Chart(ctx, {
                type: 'doughnut',
                data: {
                    labels: focus_list.map(focus => focus.focus),
                    datasets: [{
                        label: '# of practice sessions',
                        data: focus_list.map(focus => focus.count),
                        backgroundColor: [
                            'rgba(53, 88, 52, 0.2)',
                            'rgba(184, 12, 9, 0.2)',
                            'rgba(255, 255, 255, 1)',
                            'rgba(20, 40, 29, 0.2)',
                            'rgba(119, 119, 119, 0.2)',
                            'rgba(232, 241, 242, 0.2)'
                        ],
                        borderColor: [
                            'rgba(53, 88, 52, 1)',
                            'rgba(184, 12, 9, 1)',
                            'rgba(0,0,0,1)',
                            'rgba(20, 40, 29, 1)',
                            'rgba(119, 119, 119, 1)',
                            'rgba(0,0,0,1)'
                        ],
                        borderWidth: 1
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            position: 'right',
                        },
                    }
                },
            });
        } catch (e) {
            $("#no-chart").html("<p>Sorry - something has gone wrong loading your focus chart</p>");
        }
    }
};



$(document).ready(function () {

    console.log('ready')

    addChart();

    // Credit: https://tinyurl.com/2p8npant
    // init Masonry
    var $grid = $('.grid').masonry({
        // options...
    });
    // layout Masonry after each image loads
    $grid.imagesLoaded().progress(function () {
        $grid.masonry('layout');
    });

    // Prepare My Goals Buttons for Toggling
    $(".edit-goal-button").click(function () {
        const goalId = $(this).data('goal-id');
        $(`.edit-goal-range[data-goal-id="${goalId}"]`).toggle();
        $(`.goal-progress[data-goal-id="${goalId}"]`).toggle();
        $(`.save-goal-button[data-goal-id="${goalId}"]`).toggle();
        $(`.delete-goal-button[data-goal-id="${goalId}"]`).toggle();
        $(this).toggle();
    });

    $(".save-goal-button").click(function () {
        const goalId = $(this).data('goal-id');
        $(`.edit-goal-range[data-goal-id="${goalId}"]`).toggle();
        $(`.spinner-border[data-goal-id="${goalId}"]`).show();
        $(this).toggle();
    });

    $(".delete-goal-button").click(function () {
        const goalId = $(this).data('goal-id');
        $(`.edit-goal-button[data-goal-id="${goalId}"]`).toggle();
        $(`.revert-goal-button[data-goal-id="${goalId}"]`).toggle();
        $(`.confirm-delete-button[data-goal-id="${goalId}"]`).toggle();
        $(this).toggle();
    });

    $(".confirm-delete-button").click(function () {
        const goalId = $(this).data('goal-id');
        $(`.goal-progress[data-goal-id="${goalId}"]`).toggle();
        $(`.spinner-border[data-goal-id="${goalId}"]`).show();
        $(`.revert-goal-button[data-goal-id="${goalId}"]`).toggle();
        $(this).toggle();
    });

    $(".revert-goal-button").click(function () {
        const goalId = $(this).data('goal-id');
        $(`.edit-goal-button[data-goal-id="${goalId}"]`).toggle();
        $(`.delete-goal-button[data-goal-id="${goalId}"]`).toggle();
        $(`.confirm-delete-button[data-goal-id="${goalId}"]`).toggle();
        $(this).toggle();
    });

});
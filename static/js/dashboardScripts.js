  // jquery function
  // https://www.section.io/engineering-education/integrating-chart-js-in-django/

  $(document).ready(function (){
    const focus_list = JSON.parse(document.getElementById('focus').textContent);
      if (!focus_list.length) {
          $("#no-chart").html("<p><em>Log a practice</em> to start tracking where you are putting your focus.</p>")
      } else {
          try {
              var ctx = document.getElementById('focus-chart').getContext('2d');
              var myChart = new Chart(ctx, {
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
            $("#no-chart").html("<p>Sorry - something has gone wrong loading your focus chart</p>")
          }
      }
  });
window.addEventListener("DOMContentLoaded", start);

function start() {
  getData();
}

async function getData() {
  await fetch("/data", {
    method: "GET",
    headers: {
      Accept: "application/json",
    },
  })
    .then((response) => response.json())
    .then((response) => drawGraph(response));
}

function drawGraph(data) {
  let ctx = document.getElementById("chart").getContext("2d");

  let chart = new Chart(ctx, {
    type: "line",
    data: {
      labels: data.map((item) => {
        return moment(item.created_at).format("HH:MM:SS");
      }),
      datasets: [
        {
          label: "Battery Voltage",
          data: data.map((item) => item.battery_voltage),
          backgroundColor: "rgba(75, 192, 192, 0.2)",
          borderColor: "rgba(75, 192, 192, 1)",
          borderWidth: 1,
        },
      ],
    },
    options: {
      maintainAspectRatio: false,
      scales: {
        yAxes: [
          {
            ticks: {
              suggestedMin: 11,
            },
          },
        ],
      },
    },
  });
}

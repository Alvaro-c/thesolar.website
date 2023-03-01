window.addEventListener("DOMContentLoaded", start);

function start() {
  getData();
}

async function getData() {
  await fetch("/data?n=150", {
    method: "GET",
    headers: {
      Accept: "application/json",
    },
  })
    .then((response) => response.json())
    .then((response) => {
      fillTable(response);
      drawGraph(response);
    })
    .catch(() => {
      console.log("error while fetching");
    });
}

function drawGraph(data) {
  data = data.reverse();
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
          data: data.map((item) => item.load_voltage_V),
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

function fillTable(data) {
  const dateOptions = {
    weekday: "short",
    year: "numeric",
    month: "short",
    day: "numeric",
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit",
    hour12: false,
  };

  let table = document.getElementById("resultsTable");
  table.innerHTML = `<td>Time Stamp</td>
                     <td>Voltage (V)</td>
                     <td>Power (mW)</td>
                     <td>Battery Current (mA)</td>
                     <td>Solar Current (mA)</td>`;

  data.forEach((series) => {
    const date = new Date(series["created_at"]).toLocaleString(
      "de-DE",
      dateOptions
    );
    const row = table.insertRow();
    row.innerHTML = `<td>${date}</td>
                     <td>${series["load_voltage_V"].toFixed(2)}</td>
                     <td>${series["power_mW"].toFixed(2)}</td>
                     <td>${series["current_mA"].toFixed(2)}</td>
                     <td>${series["solar_panel_current_mA"].toFixed(2)}</td>`;
  });
}

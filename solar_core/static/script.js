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
    .catch((error) => {
      console.log(error);
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
          yAxisID: "y-axis-1",
        },
        {
          label: "Current flow",
          type: "bar",
          data: data.map((item) => item.current_mA * -1),
          backgroundColor: data.map((item) =>
            item.current_mA >= 0 ? "#f4c7c3" : "#b7e1cd"
          ),
          borderColor: data.map((item) =>
            item.current_mA >= 0 ? "#f4c7c3" : "#b7e1cd"
          ),
          borderWidth: 1,
          yAxisID: "y-axis-2",
        },
      ],
    },
    options: {
      maintainAspectRatio: false,
      scales: {
        yAxes: [
          {
            id: "y-axis-1",
            position: "left",
            ticks: {
              suggestedMin: 11,
            },
          },
          {
            id: "y-axis-2",
            position: "right",
            ticks: {
              beginAtZero: false,
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
                     `;

  data.forEach((series) => {
    const date = new Date(series["created_at"]).toLocaleString(
      "en-UK",
      dateOptions
    );
    let colorClass = "green";
    if (parseInt(series["current_mA"]) >= 0) {
      colorClass = "red";
    }

    const row = table.insertRow();
    row.setAttribute("class", colorClass);
    row.innerHTML = `<td>${date}</td>
                     <td>${series["load_voltage_V"].toFixed(2)}</td>
                     <td>${series["power_mW"].toFixed(2)}</td>
                     <td>${series["current_mA"].toFixed(2)}</td>
                     `;
  });
}

// Fetch weather data from the backend and update the dashboard
async function fetchWeatherData() {
    try {
        const response = await fetch('http://127.0.0.1:5000/fetch-weather');
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        console.log('Weather Data:', data);  // Log the data to check if it's fetched correctly

        // Update weather data on the page
        document.getElementById('avg-temp').textContent = data.avg_temp.toFixed(2);
        document.getElementById('max-temp').textContent = data.max_temp.toFixed(2);
        document.getElementById('min-temp').textContent = data.min_temp.toFixed(2);
        document.getElementById('dominant-condition').textContent = data.dominant_condition;

        updateTempChart(data);  // Update the chart with new data
    } catch (error) {
        console.error('Error fetching weather data:', error);  // Log any error that occurs
    }
}

// Fetch data on page load and set an interval for periodic updates
document.addEventListener('DOMContentLoaded', () => {
    createTempChart();
    fetchWeatherData();
    setInterval(fetchWeatherData, 3000);  // Fetch data every 5 minutes
});


// Initialize and update the temperature chart
let tempChart;
function createTempChart() {
    const ctx = document.getElementById('tempChart').getContext('2d');
    tempChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: [], // Times will be added dynamically
            datasets: [
                {
                    label: 'Avg Temp (°C)',
                    data: [],
                    borderColor: 'rgba(75, 192, 192, 1)',
                    fill: false
                },
                {
                    label: 'Max Temp (°C)',
                    data: [],
                    borderColor: 'rgba(255, 99, 132, 1)',
                    fill: false
                },
                {
                    label: 'Min Temp (°C)',
                    data: [],
                    borderColor: 'rgba(54, 162, 235, 1)',
                    fill: false
                }
            ]
        },
        options: {
            scales: {
                x: { title: { display: true, text: 'Time' }},
                y: { title: { display: true, text: 'Temperature (°C)' }}
            }
        }
    });
}

function updateTempChart(data) {
    const currentTime = new Date().toLocaleTimeString();

    // Add new data points
    tempChart.data.labels.push(currentTime);
    tempChart.data.datasets[0].data.push(data.avg_temp.toFixed(2));
    tempChart.data.datasets[1].data.push(data.max_temp.toFixed(2));
    tempChart.data.datasets[2].data.push(data.min_temp.toFixed(2));

    // Keep only the latest 10 data points
    if (tempChart.data.labels.length > 10) {
        tempChart.data.labels.shift();
        tempChart.data.datasets.forEach(dataset => dataset.data.shift());
    }

    tempChart.update();
}

// Fetch data on page load and set an interval for periodic updates
document.addEventListener('DOMContentLoaded', () => {
    createTempChart();
    fetchWeatherData();
    setInterval(fetchWeatherData, 300000); // Fetch data every 5 minutes
});

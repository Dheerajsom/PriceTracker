// Fetch elements from the DOM
const trackForm = document.getElementById("trackForm");
const productList = document.getElementById("productList");
const priceChartCanvas = document.getElementById("priceChart");

// Initialize price chart with Chart.js
let priceChart = new Chart(priceChartCanvas, {
  type: "line",
  data: {
    labels: [], // Date labels will go here
    datasets: [
      {
        label: "Price ($)",
        data: [], // Price data will go here
        borderColor: "#0073e6",
        backgroundColor: "rgba(0, 115, 230, 0.1)",
        fill: true,
      },
    ],
  },
  options: {
    responsive: true,
    plugins: {
      legend: {
        display: true,
        position: "top",
      },
    },
    scales: {
      x: {
        title: {
          display: true,
          text: "Date",
        },
      },
      y: {
        title: {
          display: true,
          text: "Price ($)",
        },
        beginAtZero: true,
      },
    },
  },
});

// Function to add a product to the list
function addProductToList(product) {
  const productDiv = document.createElement("div");
  productDiv.className = "product";
  productDiv.innerHTML = `
    <h3>${product.name}</h3>
    <p>Current Price: $${product.currentPrice}</p>
    <p>URL: <a href="${product.url}" target="_blank">View Product</a></p>
  `;
  productList.appendChild(productDiv);
}

// Handle form submission
trackForm.addEventListener("submit", async (event) => {
  event.preventDefault();

  const productUrl = document.getElementById("productUrl").value;
  const priceThreshold = document.getElementById("priceThreshold").value;

  try {
    // Send product tracking request to the backend
    const response = await fetch("http://localhost:5000/add-product", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ url: productUrl, threshold: priceThreshold }),
    });

    if (!response.ok) throw new Error("Failed to add product.");

    const product = await response.json();

    // Add product to the list
    addProductToList(product);

    // Clear form inputs
    trackForm.reset();
  } catch (error) {
    console.error("Error adding product:", error.message);
  }
});

// Fetch tracked products and populate the list on load
async function fetchTrackedProducts() {
  try {
    const response = await fetch("http://localhost:5000/tracked-products");
    if (!response.ok) throw new Error("Failed to fetch products.");

    const products = await response.json();

    products.forEach((product) => addProductToList(product));
  } catch (error) {
    console.error("Error fetching products:", error.message);
  }
}

// Fetch price history for the chart
async function fetchPriceHistory() {
  try {
    const response = await fetch("http://localhost:5000/price-history");
    if (!response.ok) throw new Error("Failed to fetch price history.");

    const priceHistory = await response.json();

    // Update chart data
    priceChart.data.labels = priceHistory.dates;
    priceChart.data.datasets[0].data = priceHistory.prices;
    priceChart.update();
  } catch (error) {
    console.error("Error fetching price history:", error.message);
  }
}

// On page load, fetch initial data
document.addEventListener("DOMContentLoaded", () => {
  fetchTrackedProducts();
  fetchPriceHistory();
});

let chartInstance = null;

// -----------------------------
// Main Calculation
// -----------------------------
function calculateRT() {
    const P = parseFloat(document.getElementById("profit").value);
    const U = parseFloat(document.getElementById("unemployment").value);
    const E = parseFloat(document.getElementById("energy").value);

    const alpha = parseFloat(document.getElementById("alpha").value);
    const beta = parseFloat(document.getElementById("beta").value);
    const gamma = parseFloat(document.getElementById("gamma").value);

    if (isNaN(P) || isNaN(U) || isNaN(E)) {
        alert("Please fill all numeric values.");
        return;
    }

    const RT = alpha * P + beta * U + gamma * E;

    document.getElementById("rtValue").innerText = RT.toLocaleString();

    const wf = RT * 0.40;
    const ubi = RT * 0.30;
    const green = RT * 0.30;

    document.getElementById("wfValue").innerText = wf.toLocaleString();
    document.getElementById("ubiValue").innerText = ubi.toLocaleString();
    document.getElementById("greenValue").innerText = green.toLocaleString();

    drawChart(wf, ubi, green);
}

// -----------------------------
// Draw Chart
// -----------------------------
function drawChart(wf, ubi, green) {
    const ctx = document.getElementById("taxChart").getContext("2d");

    if (chartInstance) {
        chartInstance.destroy();
    }

    chartInstance = new Chart(ctx, {
        type: "pie",
        data: {
            labels: ["Workforce Transition (40%)", "UBI-lite (30%)", "Green Infra (30%)"],
            datasets: [{
                data: [wf, ubi, green],
                backgroundColor: ["#4e79a7", "#f28e2b", "#59a14f"]
            }]
        },
        options: {
            responsive: true
        }
    });
}

// -----------------------------
// Download Chart PNG
// -----------------------------
document.addEventListener("DOMContentLoaded", () => {
    const btn = document.getElementById("downloadChartBtn");

    btn.addEventListener("click", () => {
        const canvas = document.getElementById("taxChart");
        const link = document.createElement("a");
        link.href = canvas.toDataURL("image/png");
        link.download = "AI_Responsibility_Tax_Chart.png";
        link.click();
    });
});

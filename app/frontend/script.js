async function calculateSIP() {
    const fundName = document.getElementById("fundName").value;
    const sipAmount = document.getElementById("sipAmount").value;
    const duration = document.getElementById("duration").value;

    const payload = {
        fund_name: fundName,
        monthly_sip: Number(sipAmount),
        years: Number(duration),
        expected_return_rate: 0.12
    };

    const response = await fetch("http://127.0.0.1:8000/sip/calculate", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(payload)
    });

    const data = await response.json();

    document.getElementById("resultBox").classList.remove("hidden");

    document.getElementById("rFund").innerText = data.fund_name;
    document.getElementById("rInvested").innerText = data.invested_amount;
    document.getElementById("rValue").innerText = data.expected_value;
    document.getElementById("rProfit").innerText = data.profit;
    document.getElementById("rCagr").innerText = data.cagr;
}

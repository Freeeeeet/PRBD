const apiBaseUrl = 'http://localhost:8000';

// Create Payment
document.getElementById('create-payment-form').addEventListener('submit', function (e) {
    e.preventDefault();
    const amount = document.getElementById('payment-amount').value;
    const order_id = document.getElementById('payment-order-id').value;

    fetch(`${apiBaseUrl}/payments/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ amount, order_id })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('payment-result').innerHTML = `Payment Created: ID: ${data.id}, Amount: ${data.amount}`;
    })
    .catch(error => {
        document.getElementById('payment-result').innerHTML = `Error: ${error}`;
    });
});

// Read Payment
document.getElementById('read-payment-btn').addEventListener('click', function () {
    const paymentId = document.getElementById('read-payment-id').value;

    fetch(`${apiBaseUrl}/payments/${paymentId}`)
    .then(response => response.json())
    .then(data => {
        document.getElementById('read-payment-result').innerHTML = `Payment ID: ${data.id}, Amount: ${data.amount}`;
    })
    .catch(error => {
        document.getElementById('read-payment-result').innerHTML = `Error: ${error}`;
    });
});

// Update Payment
document.getElementById('update-payment-form').addEventListener('submit', function (e) {
    e.preventDefault();
    const paymentId = document.getElementById('update-payment-id').value;
    const amount = document.getElementById('update-payment-amount').value;
    const order_id = document.getElementById('update-payment-order-id').value;

    fetch(`${apiBaseUrl}/payments/${paymentId}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ amount, order_id })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('update-payment-result').innerHTML = `Payment Updated: ID: ${data.id}, Amount: ${data.amount}`;
    })
    .catch(error => {
        document.getElementById('update-payment-result').innerHTML = `Error: ${error}`;
    });
});

// Delete Payment
document.getElementById('delete-payment-btn').addEventListener('click', function () {
    const paymentId = document.getElementById('delete-payment-id').value;

    fetch(`${apiBaseUrl}/payments/${paymentId}`, {
        method: 'DELETE'
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('delete-payment-result').innerHTML = `Payment Deleted: ${data.message}`;
    })
    .catch(error => {
        document.getElementById('delete-payment-result').innerHTML = `Error: ${error}`;
    });
});
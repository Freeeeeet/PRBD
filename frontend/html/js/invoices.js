const apiBaseUrl = 'http://localhost:8000';

// Create Invoice
document.getElementById('create-invoice-form').addEventListener('submit', function (e) {
    e.preventDefault();
    const total_amount = document.getElementById('invoice-amount').value;
    const order_id = document.getElementById('invoice-order-id').value;

    fetch(`${apiBaseUrl}/invoices/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ total_amount, order_id })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('invoice-result').innerHTML = `Invoice Created: ID: ${data.id}, Amount: ${data.total_amount}`;
    })
    .catch(error => {
        document.getElementById('invoice-result').innerHTML = `Error: ${error}`;
    });
});

// Read Invoice
document.getElementById('read-invoice-btn').addEventListener('click', function () {
    const invoiceId = document.getElementById('read-invoice-id').value;

    fetch(`${apiBaseUrl}/invoices/${invoiceId}`)
    .then(response => response.json())
    .then(data => {
        document.getElementById('read-invoice-result').innerHTML = `Invoice ID: ${data.id}, Amount: ${data.total_amount}`;
    })
    .catch(error => {
        document.getElementById('read-invoice-result').innerHTML = `Error: ${error}`;
    });
});

// Update Invoice
document.getElementById('update-invoice-form').addEventListener('submit', function (e) {
    e.preventDefault();
    const invoiceId = document.getElementById('update-invoice-id').value;
    const total_amount = document.getElementById('update-invoice-amount').value;
    const order_id = document.getElementById('update-invoice-order-id').value;

    fetch(`${apiBaseUrl}/invoices/${invoiceId}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ total_amount, order_id })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('update-invoice-result').innerHTML = `Invoice Updated: ID: ${data.id}, Amount: ${data.total_amount}`;
    })
    .catch(error => {
        document.getElementById('update-invoice-result').innerHTML = `Error: ${error}`;
    });
});

// Delete Invoice
document.getElementById('delete-invoice-btn').addEventListener('click', function () {
    const invoiceId = document.getElementById('delete-invoice-id').value;

    fetch(`${apiBaseUrl}/invoices/${invoiceId}`, {
        method: 'DELETE'
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('delete-invoice-result').innerHTML = `Invoice Deleted: ${data.message}`;
    })
    .catch(error => {
        document.getElementById('delete-invoice-result').innerHTML = `Error: ${error}`;
    });
});
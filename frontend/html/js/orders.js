const apiBaseUrl = 'http://backend:8000';

// Create Order
document.getElementById('create-order-form').addEventListener('submit', function (e) {
    e.preventDefault();
    const total_price = document.getElementById('order-price').value;
    const user_id = document.getElementById('order-user-id').value || null;

    fetch(`${apiBaseUrl}/orders/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ total_price, user_id })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('order-result').innerHTML = `Order Created: ID: ${data.id}, Price: ${data.total_price}`;
    })
    .catch(error => {
        document.getElementById('order-result').innerHTML = `Error: ${error}`;
    });
});

// Read Order
document.getElementById('read-order-btn').addEventListener('click', function () {
    const orderId = document.getElementById('read-order-id').value;

    fetch(`${apiBaseUrl}/orders/${orderId}`)
    .then(response => response.json())
    .then(data => {
        document.getElementById('read-order-result').innerHTML = `Order ID: ${data.id}, Total Price: ${data.total_price}`;
    })
    .catch(error => {
        document.getElementById('read-order-result').innerHTML = `Error: ${error}`;
    });
});

// Update Order
document.getElementById('update-order-form').addEventListener('submit', function (e) {
    e.preventDefault();
    const orderId = document.getElementById('update-order-id').value;
    const total_price = document.getElementById('update-order-price').value;
    const user_id = document.getElementById('update-order-user-id').value || null;

    fetch(`${apiBaseUrl}/orders/${orderId}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ total_price, user_id })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('update-order-result').innerHTML = `Order Updated: ID: ${data.id}, Price: ${data.total_price}`;
    })
    .catch(error => {
        document.getElementById('update-order-result').innerHTML = `Error: ${error}`;
    });
});

// Delete Order
document.getElementById('delete-order-btn').addEventListener('click', function () {
    const orderId = document.getElementById('delete-order-id').value;

    fetch(`${apiBaseUrl}/orders/${orderId}`, {
        method: 'DELETE'
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('delete-order-result').innerHTML = `Order Deleted: ${data.message}`;
    })
    .catch(error => {
        document.getElementById('delete-order-result').innerHTML = `Error: ${error}`;
    });
});
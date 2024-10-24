const apiBaseUrl = 'http://localhost:8000';

// Create Inventory
document.getElementById('create-inventory-form').addEventListener('submit', function (e) {
    e.preventDefault();
    const item_name = document.getElementById('inventory-name').value;
    const quantity = document.getElementById('inventory-quantity').value;
    const warehouse_id = document.getElementById('inventory-warehouse').value;

    fetch(`${apiBaseUrl}/inventory/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ item_name, quantity, warehouse_id })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('inventory-result').innerHTML = `Item Created: ${data.item_name} (ID: ${data.id})`;
    })
    .catch(error => {
        document.getElementById('inventory-result').innerHTML = `Error: ${error}`;
    });
});

// Read Inventory
document.getElementById('read-inventory-btn').addEventListener('click', function () {
    const itemId = document.getElementById('read-inventory-id').value;

    fetch(`${apiBaseUrl}/inventory/${itemId}`)
    .then(response => response.json())
    .then(data => {
        document.getElementById('read-inventory-result').innerHTML = `Item: ${data.item_name}, Quantity: ${data.quantity}`;
    })
    .catch(error => {
        document.getElementById('read-inventory-result').innerHTML = `Error: ${error}`;
    });
});

// Update Inventory
document.getElementById('update-inventory-form').addEventListener('submit', function (e) {
    e.preventDefault();
    const itemId = document.getElementById('update-inventory-id').value;
    const item_name = document.getElementById('update-inventory-name').value;
    const quantity = document.getElementById('update-inventory-quantity').value;
    const warehouse_id = document.getElementById('update-inventory-warehouse').value;

    fetch(`${apiBaseUrl}/inventory/${itemId}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ item_name, quantity, warehouse_id })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('update-inventory-result').innerHTML = `Item Updated: ${data.item_name}`;
    })
    .catch(error => {
        document.getElementById('update-inventory-result').innerHTML = `Error: ${error}`;
    });
});

// Delete Inventory
document.getElementById('delete-inventory-btn').addEventListener('click', function () {
    const itemId = document.getElementById('delete-inventory-id').value;

    fetch(`${apiBaseUrl}/inventory/${itemId}`, {
        method: 'DELETE'
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('delete-inventory-result').innerHTML = `Item Deleted: ${data.message}`;
    })
    .catch(error => {
        document.getElementById('delete-inventory-result').innerHTML = `Error: ${error}`;
    });
});
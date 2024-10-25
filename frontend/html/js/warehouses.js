const apiBaseUrl = '/api';

// Create Warehouse
document.getElementById('create-warehouse-form').addEventListener('submit', function (e) {
    e.preventDefault();
    const location = document.getElementById('warehouse-location').value;
    const capacity = document.getElementById('warehouse-capacity').value;

    fetch(`${apiBaseUrl}/warehouses/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ location, capacity })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('warehouse-result').innerHTML = `Warehouse Created: ID: ${data.id}, Location: ${data.location}`;
    })
    .catch(error => {
        document.getElementById('warehouse-result').innerHTML = `Error: ${error}`;
    });
});

// Read Warehouse
document.getElementById('read-warehouse-btn').addEventListener('click', function () {
    const warehouseId = document.getElementById('read-warehouse-id').value;

    fetch(`${apiBaseUrl}/warehouses/${warehouseId}`)
    .then(response => response.json())
    .then(data => {
        document.getElementById('read-warehouse-result').innerHTML = `Warehouse ID: ${data.id}, Location: ${data.location}, Capacity: ${data.capacity}`;
    })
    .catch(error => {
        document.getElementById('read-warehouse-result').innerHTML = `Error: ${error}`;
    });
});

// Update Warehouse
document.getElementById('update-warehouse-form').addEventListener('submit', function (e) {
    e.preventDefault();
    const warehouseId = document.getElementById('update-warehouse-id').value;
    const location = document.getElementById('update-warehouse-location').value;
    const capacity = document.getElementById('update-warehouse-capacity').value;

    fetch(`${apiBaseUrl}/warehouses/${warehouseId}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ location, capacity })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('update-warehouse-result').innerHTML = `Warehouse Updated: ID: ${data.id}, Location: ${data.location}`;
    })
    .catch(error => {
        document.getElementById('update-warehouse-result').innerHTML = `Error: ${error}`;
    });
});

// Delete Warehouse
document.getElementById('delete-warehouse-btn').addEventListener('click', function () {
    const warehouseId = document.getElementById('delete-warehouse-id').value;

    fetch(`${apiBaseUrl}/warehouses/${warehouseId}`, {
        method: 'DELETE'
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('delete-warehouse-result').innerHTML = `Warehouse Deleted: ${data.message}`;
    })
    .catch(error => {
        document.getElementById('delete-warehouse-result').innerHTML = `Error: ${error}`;
    });
});
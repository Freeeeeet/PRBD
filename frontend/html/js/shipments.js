const apiBaseUrl = 'http://backend:8000';

// Create Shipment
document.getElementById('create-shipment-form').addEventListener('submit', function (e) {
    e.preventDefault();
    const weight = document.getElementById('shipment-weight').value;
    const destination = document.getElementById('shipment-destination').value;
    const status = document.getElementById('shipment-status').value;

    fetch(`${apiBaseUrl}/shipments/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ weight, destination, status })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('shipment-result').innerHTML = `Shipment Created: ID: ${data.id}, Weight: ${data.weight}, Destination: ${data.destination}`;
    })
    .catch(error => {
        document.getElementById('shipment-result').innerHTML = `Error: ${error}`;
    });
});

// Read Shipment
document.getElementById('read-shipment-btn').addEventListener('click', function () {
    const shipmentId = document.getElementById('read-shipment-id').value;

    fetch(`${apiBaseUrl}/shipments/${shipmentId}`)
    .then(response => response.json())
    .then(data => {
        document.getElementById('read-shipment-result').innerHTML = `Shipment ID: ${data.id}, Destination: ${data.destination}, Status: ${data.status}`;
    })
    .catch(error => {
        document.getElementById('read-shipment-result').innerHTML = `Error: ${error}`;
    });
});

// Update Shipment
document.getElementById('update-shipment-form').addEventListener('submit', function (e) {
    e.preventDefault();
    const shipmentId = document.getElementById('update-shipment-id').value;
    const weight = document.getElementById('update-shipment-weight').value;
    const destination = document.getElementById('update-shipment-destination').value;
    const status = document.getElementById('update-shipment-status').value;

    fetch(`${apiBaseUrl}/shipments/${shipmentId}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ weight, destination, status })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('update-shipment-result').innerHTML = `Shipment Updated: ID: ${data.id}, Destination: ${data.destination}, Status: ${data.status}`;
    })
    .catch(error => {
        document.getElementById('update-shipment-result').innerHTML = `Error: ${error}`;
    });
});

// Delete Shipment
document.getElementById('delete-shipment-btn').addEventListener('click', function () {
    const shipmentId = document.getElementById('delete-shipment-id').value;

    fetch(`${apiBaseUrl}/shipments/${shipmentId}`, {
        method: 'DELETE'
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('delete-shipment-result').innerHTML = `Shipment Deleted: ${data.message}`;
    })
    .catch(error => {
        document.getElementById('delete-shipment-result').innerHTML = `Error: ${error}`;
    });
});
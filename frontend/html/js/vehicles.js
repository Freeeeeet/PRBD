const apiBaseUrl = '/api';

// Create Vehicle
document.getElementById('create-vehicle-form').addEventListener('submit', function (e) {
    e.preventDefault();
    const license_plate = document.getElementById('vehicle-license-plate').value;
    const capacity = document.getElementById('vehicle-capacity').value;
    const driver_id = document.getElementById('vehicle-driver-id').value;

    fetch(`${apiBaseUrl}/vehicles/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ license_plate, capacity, driver_id })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('vehicle-result').innerHTML = `Vehicle Created: ID: ${data.id}, License Plate: ${data.license_plate}`;
    })
    .catch(error => {
        document.getElementById('vehicle-result').innerHTML = `Error: ${error}`;
    });
});

// Read Vehicle
document.getElementById('read-vehicle-btn').addEventListener('click', function () {
    const vehicleId = document.getElementById('read-vehicle-id').value;

    fetch(`${apiBaseUrl}/vehicles/${vehicleId}`)
    .then(response => response.json())
    .then(data => {
        document.getElementById('read-vehicle-result').innerHTML = `Vehicle ID: ${data.id}, License Plate: ${data.license_plate}, Capacity: ${data.capacity}`;
    })
    .catch(error => {
        document.getElementById('read-vehicle-result').innerHTML = `Error: ${error}`;
    });
});

// Update Vehicle
document.getElementById('update-vehicle-form').addEventListener('submit', function (e) {
    e.preventDefault();
    const vehicleId = document.getElementById('update-vehicle-id').value;
    const license_plate = document.getElementById('update-vehicle-license-plate').value;
    const capacity = document.getElementById('update-vehicle-capacity').value;
    const driver_id = document.getElementById('update-vehicle-driver-id').value;

    fetch(`${apiBaseUrl}/vehicles/${vehicleId}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ license_plate, capacity, driver_id })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('update-vehicle-result').innerHTML = `Vehicle Updated: ID: ${data.id}, License Plate: ${data.license_plate}`;
    })
    .catch(error => {
        document.getElementById('update-vehicle-result').innerHTML = `Error: ${error}`;
    });
});

// Delete Vehicle
document.getElementById('delete-vehicle-btn').addEventListener('click', function () {
    const vehicleId = document.getElementById('delete-vehicle-id').value;

    fetch(`${apiBaseUrl}/vehicles/${vehicleId}`, {
        method: 'DELETE'
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('delete-vehicle-result').innerHTML = `Vehicle Deleted: ${data.message}`;
    })
    .catch(error => {
        document.getElementById('delete-vehicle-result').innerHTML = `Error: ${error}`;
    });
});
const apiBaseUrl = '/api';

// Create Driver
document.getElementById('create-driver-form').addEventListener('submit', function (e) {
    e.preventDefault();
    const name = document.getElementById('driver-name').value;

    fetch(`${apiBaseUrl}/drivers/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('driver-result').innerHTML = `Driver Created: ${data.name} (ID: ${data.id})`;
    })
    .catch(error => {
        document.getElementById('driver-result').innerHTML = `Error: ${error}`;
    });
});

// Read Driver
document.getElementById('read-driver-btn').addEventListener('click', function () {
    const driverId = document.getElementById('read-driver-id').value;

    fetch(`${apiBaseUrl}/drivers/${driverId}`)
    .then(response => response.json())
    .then(data => {
        document.getElementById('read-driver-result').innerHTML = `Driver: ${data.name}`;
    })
    .catch(error => {
        document.getElementById('read-driver-result').innerHTML = `Error: ${error}`;
    });
});

// Update Driver
document.getElementById('update-driver-form').addEventListener('submit', function (e) {
    e.preventDefault();
    const driverId = document.getElementById('update-driver-id').value;
    const name = document.getElementById('update-driver-name').value;

    fetch(`${apiBaseUrl}/drivers/${driverId}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('update-driver-result').innerHTML = `Driver Updated: ${data.name}`;
    })
    .catch(error => {
        document.getElementById('update-driver-result').innerHTML = `Error: ${error}`;
    });
});

// Delete Driver
document.getElementById('delete-driver-btn').addEventListener('click', function () {
    const driverId = document.getElementById('delete-driver-id').value;

    fetch(`${apiBaseUrl}/drivers/${driverId}`, {
        method: 'DELETE'
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('delete-driver-result').innerHTML = `Driver Deleted: ${data.message}`;
    })
    .catch(error => {
        document.getElementById('delete-driver-result').innerHTML = `Error: ${error}`;
    });
});
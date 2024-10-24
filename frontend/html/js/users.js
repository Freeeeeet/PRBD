const apiBaseUrl = 'http://localhost:8000';

// Create User
document.getElementById('create-user-form').addEventListener('submit', function (e) {
    e.preventDefault();
    const name = document.getElementById('user-name').value;
    const email = document.getElementById('user-email').value;

    fetch(`${apiBaseUrl}/users/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name, email })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('user-result').innerHTML = `User Created: ${data.name} (ID: ${data.id})`;
    })
    .catch(error => {
        document.getElementById('user-result').innerHTML = `Error: ${error}`;
    });
});

// Read User
document.getElementById('read-user-btn').addEventListener('click', function () {
    const userId = document.getElementById('read-user-id').value;

    fetch(`${apiBaseUrl}/users/${userId}`)
    .then(response => response.json())
    .then(data => {
        document.getElementById('read-user-result').innerHTML = `User: ${data.name}, Email: ${data.email}`;
    })
    .catch(error => {
        document.getElementById('read-user-result').innerHTML = `Error: ${error}`;
    });
});

// Update User
document.getElementById('update-user-form').addEventListener('submit', function (e) {
    e.preventDefault();
    const userId = document.getElementById('update-user-id').value;
    const name = document.getElementById('update-user-name').value;
    const email = document.getElementById('update-user-email').value;

    fetch(`${apiBaseUrl}/users/${userId}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name, email })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('update-user-result').innerHTML = `User Updated: ${data.name} (ID: ${data.id})`;
    })
    .catch(error => {
        document.getElementById('update-user-result').innerHTML = `Error: ${error}`;
    });
});

// Delete User
document.getElementById('delete-user-btn').addEventListener('click', function () {
    const userId = document.getElementById('delete-user-id').value;

    fetch(`${apiBaseUrl}/users/${userId}`, {
        method: 'DELETE'
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('delete-user-result').innerHTML = `User Deleted: ${data.message}`;
    })
    .catch(error => {
        document.getElementById('delete-user-result').innerHTML = `Error: ${error}`;
    });
});
-- Create users table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Create tokens table
CREATE TABLE tokens (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    token VARCHAR(255) NOT NULL,
    issued_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    expires_at TIMESTAMP NOT NULL,
    is_revoked BOOLEAN DEFAULT FALSE
);

-- Create orders table
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    total_price DECIMAL NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    user_id INTEGER REFERENCES users(id) ON DELETE SET NULL
);

-- Create shipments table
CREATE TABLE shipments (
    id SERIAL PRIMARY KEY,
    weight DECIMAL NOT NULL,
    source_location VARCHAR(255) NOT NULL,
    destination_location VARCHAR(255) NOT NULL,
    tracking_number VARCHAR(25) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Create many-to-many relationship between orders and shipments
CREATE TABLE order_shipments (
    id SERIAL PRIMARY KEY,
    order_id INTEGER REFERENCES orders(id) ON DELETE CASCADE,
    shipment_id INTEGER REFERENCES shipments(id) ON DELETE CASCADE
);


-- Create payments table
CREATE TABLE payments (
    id SERIAL PRIMARY KEY,
    amount DECIMAL NOT NULL,
    order_id INTEGER REFERENCES orders(id) ON DELETE CASCADE,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    pay_ts TIMESTAMP DEFAULT NOW()
);

-- Create invoices table
CREATE TABLE invoices (
    id SERIAL PRIMARY KEY,
    order_id INTEGER REFERENCES orders(id) ON DELETE CASCADE,
    total_amount DECIMAL NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Create delivery_status table
CREATE TABLE delivery_status (
    id SERIAL PRIMARY KEY,
    status_name VARCHAR(50) NOT NULL
);

-- Create roles table
CREATE TABLE roles (
    id SERIAL PRIMARY KEY,
    role_name VARCHAR(50) NOT NULL
);

-- Create permissions table
CREATE TABLE permissions (
    id SERIAL PRIMARY KEY,
    permission VARCHAR(50) NOT NULL
);

-- Create role_permissons table
CREATE TABLE role_permissons (
    id SERIAL PRIMARY KEY,
    role_id INTEGER REFERENCES roles(id) ON DELETE CASCADE,
    permission_id INTEGER REFERENCES permissions(id) ON DELETE CASCADE
);

-- Create user_roles table
CREATE TABLE user_roles (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    role_id INTEGER REFERENCES roles(id) ON DELETE CASCADE
);

-- Create shipment_history table
CREATE TABLE shipment_history (
    id SERIAL PRIMARY KEY,
    shipment_id INTEGER REFERENCES shipments(id) ON DELETE CASCADE,
    status_id INTEGER REFERENCES delivery_status(id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT NOW()
);

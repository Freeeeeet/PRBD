-- Create users table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Create drivers table
CREATE TABLE drivers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Create vehicles table
CREATE TABLE vehicles (
    id SERIAL PRIMARY KEY,
    license_plate VARCHAR(20) UNIQUE NOT NULL,
    capacity DECIMAL NOT NULL,
    driver_id INTEGER REFERENCES drivers(id) ON DELETE SET NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Create order_status table
CREATE TABLE order_status (
    id SERIAL PRIMARY KEY,
    status_name VARCHAR(50) NOT NULL
);

-- Create orders table
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    total_price DECIMAL NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    user_id INTEGER REFERENCES users(id) ON DELETE SET NULL,
    status_id INTEGER REFERENCES order_status(id) ON DELETE SET NULL
);

-- Create shipments table
CREATE TABLE shipments (
    id SERIAL PRIMARY KEY,
    weight DECIMAL NOT NULL,
    destination VARCHAR(255) NOT NULL,
    status VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Create many-to-many relationship between orders and shipments
CREATE TABLE order_shipments (
    order_id INTEGER REFERENCES orders(id) ON DELETE CASCADE,
    shipment_id INTEGER REFERENCES shipments(id) ON DELETE CASCADE,
    PRIMARY KEY (order_id, shipment_id)
);

-- Create warehouses table
CREATE TABLE warehouses (
    id SERIAL PRIMARY KEY,
    location VARCHAR(255) NOT NULL,
    capacity DECIMAL NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Create inventory table
CREATE TABLE inventory (
    id SERIAL PRIMARY KEY,
    item_name VARCHAR(255) NOT NULL,
    quantity INTEGER NOT NULL,
    warehouse_id INTEGER REFERENCES warehouses(id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Create payments table
CREATE TABLE payments (
    id SERIAL PRIMARY KEY,
    amount DECIMAL NOT NULL,
    order_id INTEGER REFERENCES orders(id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Create invoices table
CREATE TABLE invoices (
    id SERIAL PRIMARY KEY,
    total_amount DECIMAL NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    order_id INTEGER REFERENCES orders(id) ON DELETE CASCADE
);

-- Create delivery_status table
CREATE TABLE delivery_status (
    id SERIAL PRIMARY KEY,
    status_name VARCHAR(50) NOT NULL
);



-- Create shipment_details table
CREATE TABLE shipment_details (
    id SERIAL PRIMARY KEY,
    shipment_id INTEGER REFERENCES shipments(id) ON DELETE CASCADE,
    tracking_number VARCHAR(100) NOT NULL,
    estimated_delivery TIMESTAMP,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Create user_roles table
CREATE TABLE user_roles (
    id SERIAL PRIMARY KEY,
    role_name VARCHAR(50) NOT NULL
);

-- Create user_role_assignments table
CREATE TABLE user_role_assignments (
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    role_id INTEGER REFERENCES user_roles(id) ON DELETE CASCADE,
    PRIMARY KEY (user_id, role_id)
);

-- Create shipment_history table
CREATE TABLE shipment_history (
    id SERIAL PRIMARY KEY,
    shipment_id INTEGER REFERENCES shipments(id) ON DELETE CASCADE,
    status_id INTEGER REFERENCES delivery_status(id) ON DELETE CASCADE,
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Indexes for optimizing queries
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_vehicles_license_plate ON vehicles(license_plate);
CREATE INDEX idx_orders_user_id ON orders(user_id);
CREATE INDEX idx_shipments_destination ON shipments(destination);
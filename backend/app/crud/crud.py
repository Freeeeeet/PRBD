from fastapi import HTTPException
from sqlalchemy.orm import Session
from app import models, schemas


# Users
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user_by_id(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()
    return {"message": f"User with id {user_id} deleted successfully"}


def update_user(db: Session, user_id: int, user_data: schemas.UserCreate):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    user.name = user_data.name
    user.email = user_data.email
    db.commit()
    return user


# Orders
def get_order(db: Session, order_id: int):
    return db.query(models.Order).filter(models.Order.id == order_id).first()


def get_orders(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Order).offset(skip).limit(limit).all()


def create_order(db: Session, order: schemas.OrderCreate):
    db_order = models.Order(total_price=order.total_price, user_id=order.user_id)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


def delete_order_by_id(db: Session, order_id: int):
    order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")

    db.delete(order)
    db.commit()
    return {"message": f"Order with id {order_id} deleted successfully"}


def update_order(db: Session, order_id: int, order_data: schemas.OrderCreate):
    order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")

    order.total_price = order_data.total_price
    order.user_id = order_data.user_id
    db.commit()
    return order


# Shipments
def get_shipment(db: Session, shipment_id: int):
    return db.query(models.Shipment).filter(models.Shipment.id == shipment_id).first()


def get_shipments(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Shipment).offset(skip).limit(limit).all()


def create_shipment(db: Session, shipment: schemas.ShipmentCreate):
    db_shipment = models.Shipment(weight=shipment.weight, destination=shipment.destination, status=shipment.status)
    db.add(db_shipment)
    db.commit()
    db.refresh(db_shipment)
    return db_shipment


def delete_shipment_by_id(db: Session, shipment_id: int):
    shipment = db.query(models.Shipment).filter(models.Shipment.id == shipment_id).first()
    if shipment is None:
        raise HTTPException(status_code=404, detail="Shipment not found")

    db.delete(shipment)
    db.commit()
    return {"message": f"Shipment with id {shipment_id} deleted successfully"}


def update_shipment(db: Session, shipment_id: int, shipment_data: schemas.ShipmentCreate):
    shipment = db.query(models.Shipment).filter(models.Shipment.id == shipment_id).first()
    if shipment is None:
        raise HTTPException(status_code=404, detail="Shipment not found")

    shipment.weight = shipment_data.weight
    shipment.destination = shipment_data.destination
    shipment.status = shipment_data.status
    db.commit()
    return shipment


# Vehicles
def get_vehicle(db: Session, vehicle_id: int):
    return db.query(models.Vehicle).filter(models.Vehicle.id == vehicle_id).first()


def create_vehicle(db: Session, vehicle: schemas.VehicleCreate):
    db_vehicle = models.Vehicle(license_plate=vehicle.license_plate, capacity=vehicle.capacity,
                                driver_id=vehicle.driver_id)
    db.add(db_vehicle)
    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle


def delete_vehicle_by_id(db: Session, vehicle_id: int):
    vehicle = db.query(models.Vehicle).filter(models.Vehicle.id == vehicle_id).first()
    if vehicle is None:
        raise HTTPException(status_code=404, detail="Vehicle not found")

    db.delete(vehicle)
    db.commit()
    return {"message": f"Vehicle with id {vehicle_id} deleted successfully"}


def update_vehicle(db: Session, vehicle_id: int, vehicle_data: schemas.VehicleCreate):
    vehicle = db.query(models.Vehicle).filter(models.Vehicle.id == vehicle_id).first()
    if vehicle is None:
        raise HTTPException(status_code=404, detail="Vehicle not found")

    vehicle.license_plate = vehicle_data.license_plate
    vehicle.capacity = vehicle_data.capacity
    vehicle.driver_id = vehicle_data.driver_id
    db.commit()
    return vehicle


# Drivers
def get_driver(db: Session, driver_id: int):
    return db.query(models.Driver).filter(models.Driver.id == driver_id).first()


def create_driver(db: Session, driver: schemas.DriverCreate):
    db_driver = models.Driver(name=driver.name)
    db.add(db_driver)
    db.commit()
    db.refresh(db_driver)
    return db_driver


def delete_driver_by_id(db: Session, driver_id: int):
    driver = db.query(models.Driver).filter(models.Driver.id == driver_id).first()
    if driver is None:
        raise HTTPException(status_code=404, detail="Driver not found")

    db.delete(driver)
    db.commit()
    return {"message": f"Driver with id {driver_id} deleted successfully"}


def update_driver(db: Session, driver_id: int, driver_data: schemas.DriverCreate):
    driver = db.query(models.Driver).filter(models.Driver.id == driver_id).first()
    if driver is None:
        raise HTTPException(status_code=404, detail="Driver not found")

    driver.name = driver_data.name
    db.commit()
    return driver


# Warehouses
def get_warehouse(db: Session, warehouse_id: int):
    return db.query(models.Warehouse).filter(models.Warehouse.id == warehouse_id).first()


def create_warehouse(db: Session, warehouse: schemas.WarehouseCreate):
    db_warehouse = models.Warehouse(location=warehouse.location, capacity=warehouse.capacity)
    db.add(db_warehouse)
    db.commit()
    db.refresh(db_warehouse)
    return db_warehouse


def delete_warehouse_by_id(db: Session, warehouse_id: int):
    warehouse = db.query(models.Warehouse).filter(models.Warehouse.id == warehouse_id).first()
    if warehouse is None:
        raise HTTPException(status_code=404, detail="Warehouse not found")

    db.delete(warehouse)
    db.commit()
    return {"message": f"Warehouse with id {warehouse_id} deleted successfully"}


def update_warehouse(db: Session, warehouse_id: int, warehouse_data: schemas.WarehouseCreate):
    warehouse = db.query(models.Warehouse).filter(models.Warehouse.id == warehouse_id).first()
    if warehouse is None:
        raise HTTPException(status_code=404, detail="Warehouse not found")

    warehouse.location = warehouse_data.location
    warehouse.capacity = warehouse_data.capacity
    db.commit()
    return warehouse


# Inventory
def get_inventory(db: Session, inventory_id: int):
    return db.query(models.Inventory).filter(models.Inventory.id == inventory_id).first()


def create_inventory(db: Session, inventory: schemas.InventoryCreate):
    db_inventory = models.Inventory(item_name=inventory.item_name, quantity=inventory.quantity,
                                    warehouse_id=inventory.warehouse_id)
    db.add(db_inventory)
    db.commit()
    db.refresh(db_inventory)
    return db_inventory


def delete_inventory_item_by_id(db: Session, item_id: int):
    item = db.query(models.Inventory).filter(models.Inventory.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Inventory item not found")

    db.delete(item)
    db.commit()
    return {"message": f"Inventory item with id {item_id} deleted successfully"}


def update_inventory(db: Session, item_id: int, inventory_data: schemas.InventoryCreate):
    item = db.query(models.Inventory).filter(models.Inventory.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Inventory item not found")

    item.item_name = inventory_data.item_name
    item.quantity = inventory_data.quantity
    item.warehouse_id = inventory_data.warehouse_id
    db.commit()
    return item


# Payments
def get_payment(db: Session, payment_id: int):
    return db.query(models.Payment).filter(models.Payment.id == payment_id).first()


def create_payment(db: Session, payment: schemas.PaymentCreate):
    db_payment = models.Payment(amount=payment.amount, order_id=payment.order_id)
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment


def delete_payment_by_id(db: Session, payment_id: int):
    payment = db.query(models.Payment).filter(models.Payment.id == payment_id).first()
    if payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")

    db.delete(payment)
    db.commit()
    return {"message": f"Payment with id {payment_id} deleted successfully"}


def update_payment(db: Session, payment_id: int, payment_data: schemas.PaymentCreate):
    payment = db.query(models.Payment).filter(models.Payment.id == payment_id).first()
    if payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")

    payment.amount = payment_data.amount
    payment.order_id = payment_data.order_id
    db.commit()
    return payment


# Invoices
def get_invoice(db: Session, invoice_id: int):
    return db.query(models.Invoice).filter(models.Invoice.id == invoice_id).first()


def create_invoice(db: Session, invoice: schemas.InvoiceCreate):
    db_invoice = models.Invoice(total_amount=invoice.total_amount, order_id=invoice.order_id)
    db.add(db_invoice)
    db.commit()
    db.refresh(db_invoice)
    return db_invoice


def delete_invoice_by_id(db: Session, invoice_id: int):
    invoice = db.query(models.Invoice).filter(models.Invoice.id == invoice_id).first()
    if invoice is None:
        raise HTTPException(status_code=404, detail="Invoice not found")

    db.delete(invoice)
    db.commit()
    return {"message": f"Invoice with id {invoice_id} deleted successfully"}


def update_invoice(db: Session, invoice_id: int, invoice_data: schemas.InvoiceCreate):
    invoice = db.query(models.Invoice).filter(models.Invoice.id == invoice_id).first()
    if invoice is None:
        raise HTTPException(status_code=404, detail="Invoice not found")

    invoice.total_amount = invoice_data.total_amount
    invoice.order_id = invoice_data.order_id
    db.commit()
    return invoice
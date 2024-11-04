from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, Boolean
from sqlalchemy.orm import relationship
from .database import Base
from datetime import datetime, timedelta


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())

    tokens = relationship("Token", back_populates="user")
    orders = relationship("Order", back_populates="user")


class Token(Base):
    __tablename__ = "tokens"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    token = Column(String, nullable=False)
    issued_at = Column(DateTime, default=datetime.now())
    expires_at = Column(DateTime, default=datetime.now() + timedelta(hours=12))
    is_revoked = Column(Boolean, default=False)

    user = relationship("User", back_populates="tokens")


class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    weight = Column(Float)
    source_location = Column(String, index=True)
    destination_location = Column(String, index=True)
    tracking_number = Column(String)
    total_price = Column(Float)
    created_at = Column(DateTime, default=datetime.now())
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="orders")
    shipment_history = relationship("ShipmentHistory", back_populates="orders")

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    order_id = Column(Integer, ForeignKey("orders.id"))
    pay_ts = Column(DateTime, default=datetime.now())


class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    total_amount = Column(Float)
    created_at = Column(DateTime, default=datetime.now())


class DeliveryStatus(Base):
    __tablename__ = "delivery_status"

    id = Column(Integer, primary_key=True, index=True)
    status_name = Column(String)
    description = Column(String)


class Roles(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    role_name = Column(String)


class Permissions(Base):
    __tablename__ = "permissions"

    id = Column(Integer, primary_key=True, index=True)
    permission = Column(String)


class RolePermissons(Base):
    __tablename__ = "role_permissons"

    id = Column(Integer, primary_key=True, index=True)
    role_id = Column(Integer, ForeignKey("roles.id"))
    permission_id = Column(Integer, ForeignKey("permissions.id"))


class UserRoles(Base):
    __tablename__ = "user_roles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    role_id = Column(Integer, ForeignKey("roles.id"))


class ShipmentHistory(Base):
    __tablename__ = "shipment_history"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    status_id = Column(Integer, ForeignKey("delivery_status.id"))
    created_at = Column(DateTime, default=datetime.now())

    orders = relationship("Order", back_populates="shipment_history")

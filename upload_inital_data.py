from main import app
from application.sec import datastore
from application.models import db ,Role
from flask_security import hash_password
from werkzeug.security import generate_password_hash

with app.app_context():
    db.create_all()
    datastore.find_or_create_role(name="Admin", description="admin Role")
    datastore.find_or_create_role(name="Manager", description="Manager Role")
    datastore.find_or_create_role(name="Customer", description="Customer Role")
    db.session.commit()
    if not datastore.find_user(email="admin@email.com"):
        datastore.create_user(
            email="admin@email.com", password=generate_password_hash("12345"), roles=["Admin"])
    if not datastore.find_user(email="manager1@email.com"):
        datastore.create_user(
            email="manager1@email.com", password=generate_password_hash("manager1"), roles=["Manager"], active=False)
    if not datastore.find_user(email="customer1@email.com"):
        datastore.create_user(
            email="customer1@email.com", password=generate_password_hash("customer1"), roles=["Customer"])
    if not datastore.find_user(email="customer2@email.com"):
        datastore.create_user(
            email="customer2@email.com", password=generate_password_hash("customer2"), roles=["Customer"])
    db.session.commit()
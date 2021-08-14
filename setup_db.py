#!/usr/bin/env python3

import os
from swagger_server.models.user import User
from swagger_server.config import db

# Data to initialize database with
PEOPLE = [
    {"name": "Doug", "email": "email@dot.com"},
    {"name": "Ross", "email": "ross@dot.com", "status": 'Some status'}
]

# Delete database file if it exists currently
if os.path.exists("swagger.db"):
    os.remove("swagger.db")

# Create the database
db.create_all()

# iterate over the PEOPLE structure and populate the database
for person in PEOPLE:
    p = User(name=person['name'], email=person['email'])
    db.session.add(p)

db.session.commit()

#!/usr/bin/env python3

import os
from swagger_server.database.user import User
from swagger_server.config import db

# Data to initialize database with
PEOPLE = [
    {
        "name": "Doug",
        "email": "email@dot.com",
        "status": "Married",
        "photo_url": "https://www.muscleandfitness.com/wp-content/uploads/2015/08/what_makes_a_man_more_manly_main0.jpg?w=940&h=529&crop=1&quality=86&strip=all"
    },
    {
        "name": "Ross",
        "email": "ross@dot.com",
        "status": "Free on Monday",
        "photo_url": "https://www.muscleandfitness.com/wp-content/uploads/2015/08/what_makes_a_man_more_manly_main0.jpg?w=940&h=529&crop=1&quality=86&strip=all"
    },
    {
        "name": "Roxanne",
        "email": "roxanne@paris.com",
        "status": "Going to Berlin next week",
        "photo_url": "https://images.unsplash.com/photo-1488426862026-3ee34a7d66df?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=634&q=80"
    }
]

# Delete database file if it exists currently
if os.path.exists("swagger_server/swagger.db"):
    os.remove("swagger_server/swagger.db")

# Create the database
db.create_all()

# iterate over the PEOPLE structure and populate the database
for person in PEOPLE:
    p = User(
        name=person['name'],
        email=person['email'],
        status=person['status'],
        photo_url=person['photo_url']
    )
    db.session.add(p)

db.session.commit()

from app.database.database import SessionLocal
from app.database.models import (User, Asset)
from app.core.security import hash_password

db = SessionLocal()

users = [
    User(
        username="admin",
        email="admin@theitltd.com",
        hashed_password=hash_password(
            "Admin123"
        ),
        role="admin"
    )
]

for i in range(1, 10):
    users.append(
        User(
            username=f"user{i}",
            email=f"user{i}@theitltd.com",
            hashed_password=hash_password(
                "Password123"
            ),
            role="user"
        )
    )

db.add_all(users)
db.commit()

for user in users:
    db.refresh(user)

assets = []

for i in range(1, 11):
    assets.append(
        Asset(
            name=f"Laptop {i}",
            category="Laptop",
            serial_number=f"SN-{1000+i}",
            owner_id=users[i % len(users)].id
        )
    )

db.add_all(assets)
db.commit()

db.close()
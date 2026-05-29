import os

from db.crud import get_role_by_name, create_role, create_user, get_user_by_username
from db.database import SessionLocal, engine, Base
from user.schemas import UserCreate
from dotenv import load_dotenv

load_dotenv()

# Create tables
Base.metadata.create_all(bind=engine)


def init_db():
    db = SessionLocal()

    # Create roles if they don't exist
    if not get_role_by_name(db, "user"):
        create_role(db, "user", "Regular user")

    if not get_role_by_name(db, "admin"):
        create_role(db, "admin", "Administrator")

    if not get_role_by_name(db, "moderator"):
        create_role(db, "moderator", "Moderator")

    # Create Admin user
    admin_username = os.getenv("ADMIN_USERNAME")
    admin_password = os.getenv("ADMIN_PASSWORD")
    admin_email = os.getenv("ADMIN_EMAIL")

    admin_user = get_user_by_username(db, admin_username)

    if not admin_user:

        user_data = UserCreate(
            username=admin_username,
            email=admin_email,
            full_name="Administrator",
            password=admin_password,
        )

        create_user(db, user_data, role_name="admin")

        print("*** Admin user created ***")

    db.close()
    print("Database initialized successfully!")


if __name__ == "__main__":
    init_db()

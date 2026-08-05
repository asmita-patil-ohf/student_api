from passlib.context import CryptContext

# Create one password hashing object for the entire application
pwd_context = CryptContext(
    schemes=["bcrypt"],      # Use bcrypt hashing algorithm
    deprecated="auto"        # Automatically handle deprecated algorithms
)


def hash_password(password: str) -> str:
    return pwd_context.hash(password)
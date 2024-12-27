from sqlmodel import create_engine

# Corrected database URL
DATABASE_URL = (
    "cockroachdb+psycopg2://jay:dhEOwFiYtRthwMBhULHDLA@"
    "slick-knight-6482.j77.aws-ap-south-1.cockroachlabs.cloud:26257/defaultdb"
    "?sslmode=verify-full&sslrootcert=C:/Users/wdila/appdata/roaming/postgresql/root.crt"
)

# Create engine
engine = create_engine(DATABASE_URL)

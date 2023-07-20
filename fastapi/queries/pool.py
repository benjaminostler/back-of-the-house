import os
from psycopg_pool import ConnectionPool

pool = ConnectionPool(
    conninfo=os.environ
    ["postgresql://gastroids_user:password@localhost:8000/gastroids_db"]
    )

import os
from psycopg_pool import ConnectionPool

pool = ConnectionPool(
    conninfo=os.environ["postgresql://gastroids_user:password@db/gastroids_db"]
)

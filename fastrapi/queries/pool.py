import os
from psycopg_pool import ConnectionPool

pool = ConnectionPool(
    conninfo=os.environ["https://mar-2-pt-fastrapi.mod3projects.com/"]
)

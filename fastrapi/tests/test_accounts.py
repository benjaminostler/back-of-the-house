from fastapi.testclient import TestClient
from main import app
from queries.accounts import AccountRepository

client = TestClient(app)

totally_real_and_not_fake_db = [
    {
        "id": 1,
        "first_name": "Penny",
        "last_name": "Khung",
        "username": "lookinhungry",
        "hash_password": "8asd5g1ga2sdgs5we8g1",
        "email": "pkhung@gmail.com",
        "phone_number": "888-888-8888",
    },
    {
        "id": 2,
        "first_name": "Pat",
        "last_name": "Trick",
        "username": "mayoisaninstrument",
        "hash_password": "8asd5g1ga2sdgs5we8g1",
        "email": "pkhung@gmail.com",
        "phone_number": "888-888-8888",
    },
]

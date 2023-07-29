from fastapi.testclient import TestClient
from main import app
from queries.accounts import AccountRepository

client = TestClient(app)


class EmptyAccountRepository:
    def get_one(self, username: str):
        return {
            "id": 1,
            "first_name": "patrick",
            "last_name": "star",
            "username": "mayoisaninstrument",
            "hashed_password": "hashedbrowns",
            "email": "goofy@goober.com",
            "phone_number": "111-1111-1111",
        }

    def get_all(self):
        return []


def test_get_all_posts():
    app.dependency_overrides[AccountRepository] = EmptyAccountRepository

    response = client.get("/accounts")

    app.dependency_overrides = {}

    assert response.status_code == 200
    assert response.json() == []


def test_get_one():
    app.dependency_overrides[AccountRepository] = EmptyAccountRepository
    response = client.get("/accounts/mayoisaninstrument")
    app.dependency_overrides = {}
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "first_name": "patrick",
        "last_name": "star",
        "username": "mayoisaninstrument",
        "hashed_password": "hashedbrowns",
        "email": "goofy@goober.com",
        "phone_number": "111-1111-1111",
    }


class DeleteAccount:
    def delete(self, account_id: int):
        return True


def test_delete_account():
    app.dependency_overrides[AccountRepository] = DeleteAccount
    response = client.delete("/accounts/1")
    app.dependency_overrides = {}
    assert response.status_code == 200
    assert response.json()

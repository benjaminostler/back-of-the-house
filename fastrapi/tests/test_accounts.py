from fastapi.testclient import TestClient
from main import app
# from fastapi import HTTPException
from queries.accounts import AccountRepository, AccountIn, AccountUpdate
# import pytest

client = TestClient(app)

# # Fake data
# TEST_ACCOUNT = AccountIn(
#     first_name="Pat",
#     last_name="Trick",
#     username="mayoisaninstrument",
#     password="heyspongebob",
#     email="imastar@gmail.com",
#     phone_number="8888888888",
# )


# @pytest.fixture
# def account_repo():
#     return AccountRepository()


# def test_create(account_repo):
#     hashed_password = "hashed_password"
#     account_out = account_repo.create(TEST_ACCOUNT, hashed_password)

#     assert account_out.first_name == TEST_ACCOUNT.first_name
#     assert account_out.last_name == TEST_ACCOUNT.last_name
#     assert account_out.username == TEST_ACCOUNT.username
#     assert account_out.hashed_password == hashed_password
#     assert account_out.email == TEST_ACCOUNT.email
#     assert account_out.phone_number == TEST_ACCOUNT.phone_number
#     assert account_out.id is not None


# def test_get_all(account_repo):
#     accounts = account_repo.get_all()

#     assert len(accounts) > 0
#     assert isinstance(accounts[0].username, str)


# def test_get_one(account_repo):
#     username = "mayoisaninstrument"
#     account = account_repo.get_one(username)

#     assert account is not None
#     assert account.username == username


# def test_update(account_repo):
#     username = "mayoisaninstrument"
#     account_update = AccountUpdate(first_name="firmlygraspit")

#     updated_account = account_repo.update(username, account_update)

#     assert updated_account is not None
#     assert updated_account.first_name == "firmlygraspit"


# def test_delete_nonexistent_account(account_repo):
#     with pytest.raises(HTTPException) as exc_info:
#         account_repo.delete(12345)

#     assert exc_info.value.status_code == 404

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

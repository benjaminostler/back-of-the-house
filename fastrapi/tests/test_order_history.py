import pytest
from unittest.mock import patch
from main import app
from fastapi.testclient import TestClient
# from queries.pool import pool
from queries.orders import (
    OrderRepository,
    OrderIn,
)

client = TestClient(app)


class EmptyRepository:
    def list_orders(self):
        return []


def test_get_all_orders():
    # Arrange

    app.dependency_overrides[OrderRepository] = EmptyRepository

    response = client.get("/orders")

    # Act

    app.dependency_overrides = {}

    # Assert

    assert response.status_code == 200
    assert response.json() == []


@pytest.fixture
def setup():
    repository = OrderRepository()
    test_order = OrderIn(
        account_id="1",
        subtotal="10",
        total="11.90"
    )
    with patch("queries.pool.pool.connection") as mock_db:
        yield repository, test_order, mock_db


# @patch("queries.orders.OrderRepository.record_to_order_out")
# def test_get_order(mock_record_to_order_out, setup):
#     repository, test_order, mock_db = setup

#     # Arrange
#     mock_db.return_value.__enter__.return_value.cursor.return_value.__enter__.return_value.fetchone.return_value = (
#         None
#     )
#     mock_record_to_order_out.return_value = None

#     # Act
#     response = repository.get_order(1)

#     # Assert
#     assert response == None


# def test_create_orders(setup):
#     repository, test_order, mock_db = setup

#     # Arrangessed in 0.65s ==
#     mock_db.return_value.__enter__.return_value.cursor.return_value.__enter__.return_value.fetchone.return_value = [
#         1
#     ]

#     # Act
#     response = repository.create(test_order)

#     # Assert
#     assert response.id == 1
#     assert response.account_id == "1"
#     assert response.subtotal == "10"
#     assert response.description == "11.90"


# def test_update_orders(setup):
#     repository, test_order, mock_db = setup

#     # Arrange
#     mock_db.return_value.execute.return_value = True

#     # Act
#     response = repository.update(1, test_order)

#     # Assert
#     assert response.id == 1
#     assert response.account_id == "1"
#     assert response.subtotal == "10"
#     assert response.description == "11.90"

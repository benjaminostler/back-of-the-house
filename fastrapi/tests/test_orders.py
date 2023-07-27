from main import app
from fastapi.testclient import TestClient
from queries.orders import OrderRepository

client = TestClient(app)


class EmptyRepository:
    def list_orders(self):
        return []


class CreateOrderQueries:
    def create_order(self):
        return []


def test_init():
    assert 1 == 1


def test_get_all_orders():
    # ARRANGE

    app.dependency_overrides[OrderRepository] = EmptyRepository

    response = client.get("/orders")

    # ACT

    app.dependency_overrides = {}

    # ASSERT

    assert response.status_code == 200
    assert response.json() == []

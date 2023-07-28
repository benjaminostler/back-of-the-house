
from main import app
from fastapi.testclient import TestClient
from queries.order_items import OrderItemsRepository



client= TestClient(app)



class EmptyRepository:
  def get_all(self):
   return []


def test_get_all_order_items():
    # Arrange

    app.dependency_overrides[OrderItemsRepository] = EmptyRepository

    response = client.get("/order_items")

    # Act

    app.dependency_overrides = {}

    # Assert

    assert response.status_code == 200
    assert response.json() == []

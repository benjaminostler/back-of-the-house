from main import app
from fastapi.testclient import TestClient
from queries.menu_items import MenuItemsRepository

client = TestClient(app)


class EmptyRepository:
    def list_menu_items(self):
        return []


class CreateMenuItemQueries:
    def create_menu_item(self):
        return []


def test_init():
    assert 1 == 1


def test_get_all_menu_items():
    # ARRANGE

    app.dependency_overrides[MenuItemsRepository] = EmptyRepository

    response = client.get("/menu_items")

    # ACT

    app.dependency_overrides = {}

    # ASSERT

    assert response.status_code == 200
    assert response.json() == []

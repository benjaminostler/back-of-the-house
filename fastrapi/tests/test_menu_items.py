import pytest
from unittest.mock import patch
from main import app
from fastapi.testclient import TestClient
from queries.menu_items import MenuItemsRepository
from queries.pool import pool
from queries.menu_items import (
    MenuItemsRepository,
    MenuItemsIn,
)

client = TestClient(app)


class EmptyRepository:
    def list_menu_items(self):
        return []


class CreateMenuItemQueries:
    def create_menu_item(self):
        return []


def test_get_all_menu_items():
    # Arrange

    app.dependency_overrides[MenuItemsRepository] = EmptyRepository

    response = client.get("/menu_items")

    # Act

    app.dependency_overrides = {}

    # Assert

    assert response.status_code == 200
    assert response.json() == []


@pytest.fixture
def setup():
    repository = MenuItemsRepository()
    test_menu_item = MenuItemsIn(
        category="Beverages",
        name="Coffee",
        picture_url=None,
        description="Hot Coffee",
        price=5.0,
    )
    with patch("queries.pool.pool.connection") as mock_db:
        yield repository, test_menu_item, mock_db


@patch("queries.menu_items.MenuItemsRepository.record_to_menu_item_out")
def test_get_menu_item(mock_record_to_menu_item_out, setup):
    repository, test_menu_item, mock_db = setup

    # Arrange
    mock_db.return_value.__enter__.return_value.cursor.return_value.__enter__.return_value.fetchone.return_value = (
        None
    )
    mock_record_to_menu_item_out.return_value = None

    # Act
    response = repository.get_menu_item(1)

    # Assert
    assert response == None


def test_create_menu_items(setup):
    repository, test_menu_item, mock_db = setup

    # Arrange
    mock_db.return_value.__enter__.return_value.cursor.return_value.__enter__.return_value.fetchone.return_value = [
        1
    ]

    # Act
    response = repository.create(test_menu_item)

    # Asssert
    assert response.id == 1
    assert response.category == "Beverages"
    assert response.name == "Coffee"
    assert response.description == "Hot Coffee"
    assert response.price == 5.0


def test_update_menu_items(setup):
    repository, test_menu_item, mock_db = setup

    # Arrange
    mock_db.return_value.execute.return_value = True

    # Act
    response = repository.update(1, test_menu_item)

    # Assert
    assert response.id == 1
    assert response.category == "Beverages"
    assert response.name == "Coffee"
    assert response.description == "Hot Coffee"
    assert response.price == 5.0

from main import app
from fastapi.testclient import TestClient

client = TestClient


class EmptyTruckQueries:
    def get_trucks(self):
        return []


class CreateTruckQueries:
    def create_truck(self):
        return []


def test_init():
    assert 1 == 1

    def test_get_all_trucks():
        # ARRANGE

        app.dependency_overrides[TruckQueries] = EmptyTruckQueries

        response = client.get("/api/trucks")

        # ACT

        app.dependency_overrides = {}

        # ASSERT

        assert response.status_code == 200
        assert response.json() == {"trucks": []}

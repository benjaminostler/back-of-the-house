from main import app
from fastapi.testclient import TestClient
from queries.reservations import ReservationRepository

client = TestClient(app)

class EmptyRepository:
    def get_all(self):
        return []
    
def test_get_all_reservations():
    # Arrange

    app.dependency_overrides[ReservationRepository] = EmptyRepository
    response = client.get("/reservations")

    # Act

    app.dependency_overrides = {}

    # Assert

    assert response.status_code == 200
    assert response.json() == []
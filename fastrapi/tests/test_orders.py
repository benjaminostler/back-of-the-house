from main import app
from fastapi.testclient import TestClient
from queries.orders import OrderRepository


client= TestClient(app)



def test_init():
  assert 1==1

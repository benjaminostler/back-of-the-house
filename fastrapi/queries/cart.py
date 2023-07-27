from pydantic import BaseModel
from typing import Union
from queries.pool import pool


class Error(BaseModel):
    message: str


class CartIn(BaseModel):
    total_price: float = 0.0


class CartOut(BaseModel):
    id: int
    total_price: float = 0.0


class CartRepository:
    def create(self) -> Union[CartOut, Error]:
        query = """
            INSERT INTO cart (total_price)
            VALUES (0)
            RETURNING id, total_price;
        """
        try:
            with pool.connection() as conn:
                result = conn.execute(query)
                return CartOut(**result.fetchone())
        except Exception as e:
            print(e)
            return {"message": "Failed to create cart."}

    def get(self, cart_id: int) -> Union[CartOut, Error]:
        query = """
            SELECT id, total_price
            FROM cart
            WHERE id = :id;
        """
        try:
            with pool.connection() as conn:
                result = conn.execute(query, {"id": cart_id}).fetchone()
                return CartOut(**result)
        except Exception as e:
            print(e)
            return {"message": "Failed to get cart."}

    def update_total_price(self, cart_id: int) -> Union[CartOut, Error]:
        query = """
            UPDATE cart
            SET total_price = (
                SELECT SUM(menu_items.price * cart_items.quantity) * 1.0975
                FROM cart_items
                JOIN menu_items ON cart_items.menu_item_id = menu_items.id
                WHERE cart_items.cart_id = :cart_id
            )
            WHERE id = :cart_id
            RETURNING id, total_price;
        """
        try:
            with pool.connection() as conn:
                result = conn.execute(query, {"cart_id": cart_id})
                return CartOut(**result.fetchone())
        except Exception as e:
            print(e)
            return {"message": "Failed to update total price in cart."}

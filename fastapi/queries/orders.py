from pydantic import BaseModel
from queries.pool import pool
from typing import Optional, List, Union


class Error(BaseModel):
    message: str


class OrderIn(BaseModel):
    account_id: int
    subtotal: float
    total: float


class OrderOut(BaseModel):
    id: int
    account_id: int
    subtotal: float
    total: float


class OrderRepository(BaseModel):
    def order_in_to_out(self, id: int, orders: OrderIn):
        old_data = orders.dict()
        return OrderOut(id=id, **old_data)

    def record_to_order_out(self, record):
        return OrderOut(
            id=record[0],
            account_id=record[1],
            subtotal=record[2],
            total=record[3],
            )

    def get_orders(self) -> Union[List[OrderOut], Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id,
                            account_id,
                            subtotal,
                            total
                        FROM orders

                        ORDER BY id
                        """
                    )
                    return [
                        self.record_to_order_out(record)
                        for record in result
                    ]

        except Exception:
            return {"message": "Could not get all orders"}

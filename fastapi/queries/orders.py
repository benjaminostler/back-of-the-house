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
    def get_order(self, orders_id: int) -> Optional[OrderOut]:
        try:
            # connect the database
            with pool.connection() as conn:
                # get a cursor (something to run SQL with)
                with conn.cursor() as db:
                    db.execute(
                        """
                        SELECT id,
                            account_id,
                            subtotal,
                            total
                        FROM orders
                        WHERE id = %s
                        """,
                        [orders_id]
                    )
                    record = db.fetchone()
                    if record is None:
                        return {"message": "Order not found"}
                    return self.record_to_order_out(record)
        except Exception as e:
            print(e)
            return {"message": "Could not get that order"}

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

    def delete(self, orders_id: int) -> bool:
        try:
            # connect the database
            with pool.connection() as conn:
                # get a cursor (something to run SQL with)
                with conn.cursor() as db:
                    db.execute(
                        """
                        DELETE from orders
                        WHERE id = %s
                        """,
                        [orders_id]
                    )
                    return True
        except Exception as e:
            print(e)
            return False

    def create(self, orders: OrderIn) -> OrderOut:
        try:
            # connect the database
            with pool.connection() as conn:
                # get a cursor (something to run SQL with)
                with conn.cursor() as db:
                    # Run our INSERT statement
                    result = db.execute(
                        """
                        INSERT INTO orders
                            (
                            account_id,
                            subtotal,
                            total
                            )
                        VALUES
                            (%s, %s, %s)
                        RETURNING id;
                        """,
                        [
                            orders.account_id,
                            orders.subtotal,
                            orders.total
                        ]
                    )
                    id = result.fetchone()[0]
                    # Return new data
                    return self.order_in_to_out(id, orders)
        except Exception as e:
            print(e)
            return {"message": "Could not create new Order"}

    def update(
        self, orders_id: int, orders: OrderIn
    ) -> Union[Error, List[OrderOut]]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        UPDATE orders
                        SET
                        subtotal=%s,
                        total=%s,
                        WHERE id = %s

                        """,
                        [

                           orders.subtotal,
                           orders.total,
                           orders_id,
                        ],
                    )
                    old_data = orders.dict()
                    return OrderOut(id=orders_id, **old_data)
        except Exception as e:
            print(e)
            return {"message": "Could not update order."}

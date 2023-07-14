from pydantic import BaseModel
from queries.pool import pool
from typing import Optional, List, Union

class Error(BaseModel):
    message: str

class OrderIn(BaseModel):
    menu_item_id: int
    category:str
    quantity: int
    price_usd: float

class OrderOut(BaseModel):
    id: int
    menu_item_id: int
    category:str
    quantity: int
    price_usd: float


class OrderRepository(BaseModel):
    def get_one(self, order_id: int) -> Optional[OrderOut]:
        try:
            # connect the database
            with pool.connection() as conn:
                # get a cursor (something to run SQL with)
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id
                             , menu_item_id
                             , category
                             , quantity
                             ,price_usd
                        FROM orders
                        WHERE id = %s
                        """,
                        [order_id]
                    )
                    record = result.fetchone()
                    return self.record_to_order_out(record)
        except Exception as e:
            print(e)
            return {"message": "Could not get that order"}

    def get_all(self, id) -> Union[Error, OrderOut]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT order_id, username, order_total, order_items
                        FROM orders
                        WHERE order_id = id
                        ORDER BY order_id
                        """
                    )
                    return [
                        OrderOut(
                            order_id=entry[0],
                            username=entry[1],
                            order_total=entry[2],
                            order_items=entry[3],
                        )
                        for entry in db
                    ]

        except Exception:
            return {"message": "Could not get all orders"}

    def delete(self, order_id: int) -> bool:
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
                        [order_id]
                    )
                    return True
        except Exception as e:
            print(e)
            return False

    def create(self, order: OrderIn) -> OrderOut:
        try:
            # connect the database
            with pool.connection() as conn:
                # get a cursor (something to run SQL with)
                with conn.cursor() as db:
                    # Run our INSERT statement
                    result = db.execute(
                        """
                        INSERT INTO orders
                            (menu_item_id, category, quantity, price_usd)
                        VALUES
                            (%s, %s, %s, %s)
                        RETURNING id;
                        """,
                        [order.menu_item_id, order.category, order.quantity, order.price_usd]
                    )
                    id = result.fetchone()[0]
                    # Return new data
                    return self.order_in_to_out(id,order)
        except Exception as e:
            print(e)
            return {"message": "Could not create new Order"}

    def update(
        self, order_id: int, order: OrderIn
    ) -> Union[Error, List[OrderOut]]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        UPDATE orders
                        SET menu_item_id = %s,
                        category = %s,
                        quantity = %s,
                        price_usd = %s,
                        WHERE id = %s

                        """,
                        [
                           order.menu_item_id,
                           order.category,
                           order.quantity,
                           order.price_usd,
                           order_id,
                        ],
                    )
                    old_data = order.dict()
                    return OrderOut(id=order_id, **old_data)
        except Exception as e:
            print(e)
            return {"message": "Could not update order."}

def order_in_to_out(self, id: int, orders: OrderIn):
        old_data = orders.dict()
        return OrderOut(id=id, **old_data)


def record_to_order_out(self, record):
        return OrderOut(
            id=record[0],
            menu_item_id=record[1],
            category=record[2],
            quantity=record[3],
            price_usd=[4]
        )

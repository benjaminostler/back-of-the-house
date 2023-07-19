# Raymond:
# update
# delete
# Benjamin:
# create
# get all
from pydantic import BaseModel, validator
from queries.pool import pool
from typing import List, Union


class Error(BaseModel):
    message: str


class OrderItemsIn(BaseModel):
    orders_id: int
    menu_item_id: int
    quantity: int

    @validator("menu_item_id", "quantity", pre=True)
    def ensure_int(cls, v):
        if not isinstance(v, int):
            raise ValueError(f"{v} is not a valid integer")
        return v


class OrderItemsOut(BaseModel):
    id: int
    orders_id: int
    menu_item_id: int
    quantity: int


class OrderItemsRepository(BaseModel):
    def order_items_in_to_out(self, id: int, order_items: OrderItemsIn):
        old_data = order_items.dict()
        return OrderItemsOut(id=id, **old_data)

    def record_to_order_items_out(self, record):
        return OrderItemsOut(
            id=record[0],
            orders_id=record[1],
            menu_item_id=[2],
            quantity=[3],
        )

    def get_all(self) -> Union[Error, List[OrderItemsOut]]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        SELECT id,
                            orders_id,
                            menu_item_id,
                            quantity,
                        FROM order_items
                        ORDER BY id
                        """
                    )
                    return [
                        OrderItemsOut(
                            id=entry[0],
                            orders_id=entry[1],
                            menu_item_id=entry[3],
                            quantity=entry[4],
                        )
                        for entry in db
                    ]
        except Exception:
            return {"message": "Could not get all order items"}

    def create(self, order_items: OrderItemsIn) -> OrderItemsOut:
        try:
            # connect the database
            with pool.connection() as conn:
                # get a cursor (something to run SQL with)
                with conn.cursor() as db:
                    # Run our INSERT statement
                    result = db.execute(
                        """
                        INSERT INTO order_items
                            (
                            orders_id
                            , menu_item_id
                            , quantity
                            )
                        VALUES
                            (%s, %s, %s)
                        RETURNING id
                        , orders_id
                        , menu_item_id
                        , quantity;
                        """,
                        [
                            order_items.orders_id,
                            order_items.menu_item_id,
                            order_items.quantity,
                        ],
                    )
                    record = result.fetchone()
                    return self.record_to_order_items_out(record)
        except Exception as e:
            print("e", e)
            return {"message": "Could not create new order items."}

    def update(
        self, order_items_id: int, order_items: OrderItemsIn
    ) -> Union[OrderItemsOut, Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        UPDATE order_items
                        SET
                            orders_id = %s,
                            menu_item_id = %s,
                            quantity = %s,
                        WHERE id = %s

                        """,
                        [
                            order_items.orders_id,
                            order_items.menu_item_id,
                            order_items.quantity,
                            order_items_id,
                        ],
                    )
                    order_items.id = order_items_id
                    return order_items
        except Exception as e:
            print(e)
            return {"message": "Could not update order items."}

    def delete(self, order_item_id: int) -> bool:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        DELETE FROM order_items
                        WHERE id = %s
                        """,
                        [order_item_id],
                    )
            return True
        except Exception as e:
            print(e)
            return False

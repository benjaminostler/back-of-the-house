from pydantic import BaseModel
from queries.pool import pool
from typing import Optional 


class Error(BaseModel):
    message: str


class InvoiceIn(BaseModel):
    order_id: int
    subtotal: float
    total: float

class InvoiceOut(BaseModel):
    id: int
    order_id: int
    subtotal: float
    total: float

class InvoiceRepository:
    def get_one(self, invoice_id: int) -> Optional[InvoiceOut]:
        try:
            # connect the database
            with pool.connection() as conn:
                # get a cursor (something to run SQL with)
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id
                             , order_id
                             , subtotal
                             , total
                        FROM invoice
                        WHERE id = %s
                        """,
                        [invoice_id]
                    )
                    record = result.fetchone()
                    return self.record_to_invoice_out(record)
        except Exception as e:
            print(e)
            return {"message": "Could not get that invoice"}    
        

    def delete(self, invoice_id: int) -> bool:
        try:
            # connect the database
            with pool.connection() as conn:
                # get a cursor (something to run SQL with)
                with conn.cursor() as db:
                    db.execute(
                        """
                        DELETE from invoice
                        WHERE id = %s
                        """,
                        [invoice_id]
                    )
                    return True
        except Exception as e:
            print(e)
            return False
        
    def create(self, invoice: InvoiceIn) -> InvoiceOut:
        try:
            # connect the database
            with pool.connection() as conn:
                # get a cursor (something to run SQL with)
                with conn.cursor() as db:
                    # Run our INSERT statement
                    result = db.execute(
                        """
                        INSERT INTO invoice
                            (order_id, subtotal, total)
                        VALUES
                            (%s, %s, %s)
                        RETURNING id;
                        """,
                        [invoice.order_id, invoice.subtotal, invoice.total]
                    )
                    id = result.fetchone()[0]
                    # Return new data
                    return self.invoice_in_to_out(id, invoice)
        except Exception as e:
            print(e)
            return {"message": "Could not create new invoice"}
        
            
    def invoice_in_to_out(self, id: int, invoice: InvoiceIn):
        old_data = invoice.dict()
        return InvoiceOut(id=id, **old_data)

    
    def record_to_invoice_out(self, record):
        return InvoiceOut(
            id=record[0],
            order_id=record[1],
            subtotal=record[2],
            total=record[3]
        )
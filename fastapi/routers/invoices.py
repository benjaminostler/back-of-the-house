from fastapi import APIRouter, Depends, Response
from queries.invoices import InvoiceIn, InvoiceRepository,  InvoiceOut, Error
from typing import Union, Optional

router = APIRouter()

@router.post("/invoices", response_model=Union[InvoiceOut, Error])
def create_invoice(
    invoice: InvoiceIn,
    response: Response,
    repo: InvoiceRepository = Depends()
):
    return repo.create(invoice)

@router.delete("/invoices/{invoice_id}", response_model=bool)
def delete_invoice(
    invoice_id: int,
    repo: InvoiceRepository = Depends(),
) -> bool:
    return repo.delete(invoice_id)

@router.get("/invoices/{invoice_id}", response_model=Optional[InvoiceOut])
def get_one_invoice(
        invoice_id: int,
        repo: InvoiceRepository = Depends(),
) -> InvoiceOut:
    return repo.get_one(invoice_id)
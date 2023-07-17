from fastapi import APIRouter, Depends, Response
from queries.invoices import InvoiceIn, InvoiceRepository,  InvoiceOut, Error
from typing import Union, Optional, List

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

@router.get("/invoices", response_model=Union[Error, List[InvoiceOut]])
def list_invoices(
    repo: InvoiceRepository = Depends(),
):
    return repo.list_invoices()

@router.put("/invoices/{invoice_id}", response_model=Union[InvoiceOut, Error])
def update_invoice(
    invoice_id: int,
    menu_item_id: InvoiceIn,
    repo: InvoiceRepository = Depends(),
) -> Union[Error, InvoiceOut]:
    return repo.update(invoice_id, menu_item_id)

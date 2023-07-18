
@router.get("/invoices/{invoice_id}", response_model=Optional[InvoiceOut])
def get_one_invoice(
        invoice_id: int,
        repo: InvoiceRepository = Depends(),
) -> InvoiceOut:
    return repo.get_one(invoice_id)
invoices = [
    {
        "invoice_id": "INV-101",
        "vendor": "ABC Ltd",
        "amount": 1500.0,
        "status": "Paid"
    },
    {
        "invoice_id": "INV-102",
        "vendor": "Test Ltd",
        "amount": 4500.0,
        "status": "Pending"
    },
      {
            "invoice_id": "INV-101",
            "vendor": "ABC Ltd",
            "amount": 1500.0,
            "status": "Paid"
        },
        
]
#Now I need to change the index_id of 3rd value not the first one. If I give index_id = INV-101, it will refer 2 values.
for index, invoice in enumerate(invoices):
    if invoice[2] == 2:
        invoices[index]["invoice_id"]="INV-102"
    print(index, invoice)

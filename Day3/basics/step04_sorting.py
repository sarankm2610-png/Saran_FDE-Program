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
sorted_invoices = sorted(invoices, key=lambda invoice: invoice["amount"], reverse =True)
print(sorted_invoices[0]["amount"])
invoice = {
    "invoice_id": 1,
    "amount": 1200,
    "status": "pending"
}
#print(invoice["vendor"])
print(invoice.get("vendor"))
print(invoice.get("vendor", "UNKNOWN"))
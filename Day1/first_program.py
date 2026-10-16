invoice_amount = 50000 
if (invoice_amount>50000):
    approver= "Manager and director"
elif(invoice_amount>25000):
    approver= "Manager"
else:
    approver= "Supervisor"

print(approver)
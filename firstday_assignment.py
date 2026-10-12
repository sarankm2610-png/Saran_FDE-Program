import csv
total_rows = 0
valid_amounts = 0
invalid_amounts = 0
matching_invoices = 0
with open('data/homework_invoices.csv', newline='') as file:
    csv_reader = csv.DictReader(file)

    with open('data/output.csv', 'w', newline='') as output_file:
        csv_writer = csv.DictWriter(
            output_file,
            fieldnames=csv_reader.fieldnames
        )

        csv_writer.writeheader()

        for row in csv_reader:
            total_rows += 1
            amount = row['amount']

            try:
                amount = float(amount)
                valid_amounts += 1

                if amount > 100000:
                    csv_writer.writerow(row)
                    matching_invoices += 1

            except (ValueError, TypeError):
                invalid_amounts += 1
                print(
                    f"Invalid amount for invoice "
                    f"{row.get('invoice_id', 'Unknown')}: {row['amount']}"
                )

print("Output file created successfully")

print("\nSummary")
print("-------")
print(f"Total rows: {total_rows}")
print(f"Valid amounts: {valid_amounts}")
print(f"Invalid amounts: {invalid_amounts}")
print(f"Invoices with amount > 100000: {matching_invoices}")

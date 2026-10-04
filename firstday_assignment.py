import csv

with open('data/homework_invoices.csv') as file:
    csv_reader = csv.DictReader(file)

    with open('data/output.csv', 'w', newline='') as output_file:
        csv_writer = csv.DictWriter(
            output_file,
            fieldnames=csv_reader.fieldnames
        )

        csv_writer.writeheader()

        for row in csv_reader:
            amount = row['amount']

            if amount.isdigit() and int(amount) > 100000:
                csv_writer.writerow(row)

print("Output file created successfully")
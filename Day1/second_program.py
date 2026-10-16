
Employees = [{"employee_id": 100, "name": "saranya", "salary": 10000},
            {"employee_id": 101, "name": "kumar", "salary": 20000},
            {"employee_id": 102, "name": "anandkumar", "salary": 30000},
            {"employee_id": 103, "name": "srinivasan", "salary": 40000},
            {"employee_id": 104, "name": "arul", "salary": 50000}]
for employee in Employees:
    if len(employee["name"])>6 and employee["salary"]<25000:
        print(employee["name"])
        print(employee["salary"])
          

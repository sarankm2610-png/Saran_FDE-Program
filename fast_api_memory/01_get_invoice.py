from fastapi import FastAPI
app=FastAPI()
employees=[{"employee name": "Saran", "id": 5000},
           {"employee name": "kumar", "id": 5001},
           {"employee name": "Anil", "id": 5002},
           {"employee name": "Muthu", "id": 5003}]
@app.get("/employees")
def get_employees():
    return employees

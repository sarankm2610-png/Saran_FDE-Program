from decimal import Decimal
name ="Saran kumar"
age = 17
is_student=True
height=5.9
weight=None
money = Decimal(2000)
print(f"Name is {name}")
print(f"Age is {age}")
print(f"student is {is_student}")
print(f"Height is {height}")
print(f"Weight is {weight}")

print(f"Name is {type(name)}")
print(f"Age is {type(age)}")
print(f"student is {type(is_student)}")
print(f"Height is {type(height)}")
print(f"Weight is {type(weight)}")
print (f"Money is {type(money)}")
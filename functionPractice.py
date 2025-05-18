def greet(name):
    print(f"Hello, {name}")
greet("Ravi")

def add(num1,num2):
    total=num1+num2
    return total
total_cost=add(5,3)
print(total_cost)

def greet_user(name,greet="Hello,"):
    print(f"{greet} {name}")
greet_user("Sita")
greet_user("Sita", "Welcome")

def add_numbers(*num):
    total=sum(num)
    return total
print(add_numbers(1, 2, 3))
print(add_numbers(10, 20))

def print_info(**info):
    for key,value in info.items():
        print(f"{key}: {value}")
print_info(name="Ravi", age=25, city="Delhi")

def calculator(num1,num2,operator):
    if operator=="+":
        total=num1+num2
    elif operator=="-":
        total=num1-num2
    elif operator=="*":
        total=num1*num2
    else:
        total=num1/num2
    return total
print(calculator(10, 5, operator='+'))
print(calculator(10, 5, operator='*'))

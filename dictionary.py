labour_with_cost={"Mahesh":500,
                 "Ramesh":400,
                  "Anil":400}
# #Update
labour_with_cost["suresh"]=600

print(labour_with_cost)

print(labour_with_cost.items())

#iterate to display both value and key
for name in labour_with_cost:
    print(name,labour_with_cost[name])

#using items()
for key,value in labour_with_cost.items():
    print(key,value)

#Nested dictoinaries
family = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

#accessing
print(family["child2"]["name"])

#loop
for child in family:
    print(child)

for x,obj in family.items():
    print(x)
    for y in obj:
        print(y,obj[y])

total_labor_cost=0
num_of_days=50
print(labour_with_cost)
for name in labour_with_cost:
    if name== "Mahesh":
        total_labor_cost = (num_of_days-3)*labour_with_cost[name]
        print(f'''Total labor cost of {name} is {total_labor_cost}''')
    elif name== "suresh":
        total_labor_cost=(num_of_days-7)*labour_with_cost[name]
        print(f'''Total labor cost of {name} is {total_labor_cost}''')
    else:
        total_labor_cost=num_of_days*labour_with_cost[name]
        print(f'''Total labor cost of {name} is {total_labor_cost}''')



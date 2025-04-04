n = int(input("Enter a numbererr"))

table = [n*i for i in range(1,11)]
print(table)

with open('tables.txt' , 'w') as f:
    f.write(str(table))
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn=sqlite3.connect("NorthWind.db")

#Obteniendo los 10 primeros productos mas rentables
query= """
select ProductName, SUM(Price * Quantity) as Revenue
from OrderDetails od 
join Products p on od.ProductID = p.ProductID

group by od.ProductID
order by Revenue DESC
limit 10
"""
top_products = pd.read_sql_query(query,conn)


top_products.plot(x= "ProductName", y="Revenue", kind= "bar", figsize=(10,5), legend=False)

plt.title("10 productos mas rentables")
plt.xlabel("Productos")
plt.ylabel("Revenue")
plt.xticks(rotation= 90)
plt.show()


#Obteniendo los 10 primeros empleados mas rentables

query2= """
Select FirstName|| " "  || LastName as employee, count(*) as total
from Orders o 
join Employees e on e.EmployeeID = o.EmployeeID
group by o.EmployeeID
order by total
"""

top_employees= pd.read_sql_query(query2, conn)

top_employees.plot(x="employee", y="total", kind="bar", figsize=(10,5), legend=False)

plt.title("Los 10 empleados mas destacados")
plt.xlabel("Empleados")
plt.ylabel("Total recaudado")
plt.xticks(rotation=45)
plt.show()



#Obteniendo los 10 productos mas caros

query3= """
select ProductName, Price from Products 
order by Price Desc
limit 10
"""

top_products_expensive= pd.read_sql_query(query3, conn)

top_products_expensive.plot(x="ProductName", y="Price", kind="bar", figsize=(10,5), legend=False)

plt.title("10 productos mas caros")
plt.xlabel("Productos")
plt.ylabel("Precio")
plt.xticks(rotation=45)
plt.show()

#Obteniendo los clientes mas frecuentes 

query4= """

select CustomerName, Count(*) as total
from Customers C
join Orders o on C.CustomerID = o.CustomerID

Group by C.CustomerID
order by total DESC
limit 10
"""

top_customers= pd.read_sql_query(query4, conn)
top_customers.plot(x="CustomerName", y="total", kind="bar", figsize=(10,5), legend=False)

plt.title("Clientes mas frecuentes")
plt.xlabel("Clientes")
plt.ylabel("Compras")
plt.xticks(rotation= 45)
plt.show()
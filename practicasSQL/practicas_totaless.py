import sqlite3
import pandas as pd 
import matplotlib.pyplot as plt


with sqlite3.connect("NorthWind.db") as conn1:

# Obteniendo los productos de categoria 3 y 5
    query1="select ProductName from Products where CategoryID= 3 or CategoryID= 5 Order by Random() limit 5"
    cursor=conn1.cursor()
    cursor.execute(query1)
    results= cursor.fetchall()
    results_df= pd.DataFrame(results)
    print(results_df)




    
    #PROVEEDORES QUE MAS PRODUCTOS HAN TRAIDO 
    query2= """
    
    select SupplierName, Count(*) as Total
    from Suppliers S 
    join Products p on S.SupplierID= p.SupplierID 
    group by S.SupplierID
    order by Total Desc
    """
    cursor.execute(query2)
    results1= cursor.fetchall()
    results_df1= pd.DataFrame(results1)
    print(results_df1)
    
    #Find employees who have processed orders for customers in France.
    
    query3= """
    SELECT DISTINCT e.FirstName || ' ' || e.LastName AS EmployeeName
    FROM Employees e
    JOIN Orders o ON e.EmployeeID = o.EmployeeID
    JOIN Customers c ON o.CustomerID = c.CustomerID
    WHERE c.Country = 'France'
    """
    cursor.execute(query3)
    results2= cursor.fetchall()
    results_df2= pd.DataFrame(results2)
    print(results_df2)
    
    
    # Ganancias Del año 1997
    
    query4= """
    select OrderDate, Sum(Price * Quantity) as Total_ganado
    from Orders o
    join OrderDetails od on o.OrderID= od.OrderID
    join Products p on p.ProductID= od.ProductID
    where OrderDate BETWEEN	"1997-01-01" and "1997-12-31"
    group by OrderDate
    order by Total_ganado DESC
    """
    cursor.execute(query4)
    results3= cursor.fetchall()
    results_df3= pd.DataFrame(results3)
    print(results_df3)
    
    
      



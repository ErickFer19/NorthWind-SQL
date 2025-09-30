import sqlite3
import pandas as pd

square= lambda n : n*n


with sqlite3.connect("NorthWind.db") as conn:
    conn.create_function("square",1,square)
    cursor= conn.cursor()
    cursor.execute("select *, square(Price) as Precio_al_cuadrado from Products  where Price is not null")
    results= cursor.fetchall()
    results_df= pd.DataFrame(results)
    print(results_df)


import psycopg2
# conn=psycopg2.connect(
#     database="my_duka", user='postgres', password='@Carol#2023',
#     host='localhost', port= '5432'
# )
# #Creating a cursor object using the cursor() method
# cursor = conn.cursor()

# #Executing an MYSQL function using the execute() method
# #cursor.execute("select * from products")
# cursor.execute("select * from sales")

# #Fetch a single row using fetchone() method.
# data = cursor.fetchall()
# print("Connection established to: ",data)

# #Closing the connection
# conn.close()
#once you see the products, now redo the code and have a function called get_data that:
#take in table_name as argument, fetches all records, return list of records

def get_data(p):
    conn=psycopg2.connect(
    database="my_duka", user='postgres', password='@Carol#2023',
    host='localhost', port= '5432')
    cursor = conn.cursor()
    t="select * from "+ ""+p
    cursor.execute(t)
    list_of_records= cursor.fetchall()
    return list_of_records

prods= get_data("products")
print(prods)
sales= get_data("sales")
print(sales)


#use the function by calling it as below; prods= get_data("products"), sales= get_data("sales"), #prints(prods)
#create a repository called sales_system 

#you can use string formating on cursor.execute(f"select * from {p}")
conn=psycopg2.connect(database="my_duka", user='postgres', password='@Carol#2023',host='localhost', port= '5432')
def insert_data(table_name,columns, values):
    try:
        cursor = conn.cursor()
        placeholders= ','.join(['%s'] * len(values))
        insert_query= f"INSERT INTO {table_name} ({','.join(columns)}) VALUES ({placeholders})"
        cursor.execute(insert_query, values)
        conn.commit()
        print(f"Data inserted into {table_name} successfully")
    except (Exception, psycopg2.Error) as error:
        print(f"Failed to insert into {table_name}: {error}")
    finally:
        conn.close()
columns= ('productname', 'buying_price', 'selling_price', 'stock_quantity')
values= ('maize', 120, 220, 500)

insert_data('sales', columns, values)
conn.close()
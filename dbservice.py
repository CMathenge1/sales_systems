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

    


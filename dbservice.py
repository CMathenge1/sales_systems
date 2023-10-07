import psycopg2

from datetime import datetime
conn=psycopg2.connect(
    database="my_duka", user='postgres', password='@Carol#2023',
    host='localhost', port= '5432'
)
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

def get_data(t_name):
    cursor = conn.cursor()
    cursor.execute(f"select * from {t_name}")
    list_of_records= cursor.fetchall()
    return list_of_records

# prods= get_data("products")
# print(prods)
# sales= get_data("sales")
# print(sales)


#use the function by calling it as below; prods= get_data("products"), sales= get_data("sales"), #prints(prods)
#create a repository called sales_system 

#you can use string formating on cursor.execute(f"select * from {p}")

# def insert_data(table_name,columns, values):
#     try:
#         cursor = conn.cursor()
#         placeholders= ','.join(['%s'] * len(values))
#         insert_query= f"INSERT INTO {table_name} ({','.join(columns)}) VALUES ({placeholders})"
#         cursor.execute(insert_query, values)
#         conn.commit()
#         print(f"Data inserted into {table_name} successfully")
#     except (Exception, psycopg2.Error) as error:
#         print(f"Failed to insert into {table_name}: {error}")
#     finally:
#         conn.close()

def ins_product(values):
    cursor=conn.cursor()
    cursor.execute("insert into products (productname, buying_price, selling_price, stock_quantity) values(%s,%s,%s,%s)", values)
    conn.commit()

def insert_sale(sal):
    cursor=conn.cursor()
    insert_query="insert into sales (pid,quantity,created_at) values(%s,%s,now())"
    cursor.execute(insert_query,sal)
    conn.commit()

def calculate_profit():
    cursor=conn.cursor()
    profit_query="""Select DATE(created_at) as date,
      sum((selling_price-buying_price)*quantity) as profit
      from sales join products on sales.pid=products.id
      group by date
      order by date"""
    cursor.execute(profit_query)
    records= cursor.fetchall()
    return(records)

def check_email_exists(x):
    cursor=conn.cursor()
    cursor.execute("Select exists(select 1 from users where email=%s)", x)
    exists= cursor.fetchone()[0]
    return (exists)

def email_password_match(email, password):
    cursor= conn.cursor()
    cursor.execute("Select id from users where email=%s and password=%s", (email, password))
    result= cursor.fetchone()
    if result is not None:
        id= result[0]
        return id
    else:
        return None
    
def create_users(full_name, email, password):
    cursor= conn.cursor()
    create_query= "insert into users (full_name, email, password) values(%s, %s,%s)"
    cursor.execute(create_query, (full_name, email,password))
    conn.commit()
    
# columns= ('productname', 'buying_price', 'selling_price', 'stock_quantity')
# values= ('amaize', 120, 220, 500)

# insert_product(values)
# conn.close()


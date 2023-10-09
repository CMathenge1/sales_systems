from flask import Flask, render_template, request, redirect, flash, session
from dbservice import get_data
from dbservice import ins_product, calculate_profit
from dbservice import insert_sale, create_users, check_email_exists, email_password_match
app=Flask(__name__)
app.secret_key= "Carol"


# def login_check():
#     if session['email'] !=None:
#         return redirect ("/dashboard")
#     return redirect("/login")


@app.route("/")
def sales_system():
    return render_template("index.html")

@app.route("/dashboard")
def dashboad():
    dates=[]
    profits=[]
    for i in calculate_profit():
        dates.append(str(i[0]))
        profits.append(float(i[1]))
    return render_template("dashboard.html", dates=dates, profits=profits)

@app.route("/products")
def products():
    prods=get_data("products")
    return render_template("products.html", myproducts=prods)

@app.route("/insert_product", methods=["Post"])
def insert_product():
    name= request.form['productname']
    bprice= request.form['buying_price']
    sprice= request.form['selling_price']
    squantity= request.form['stock_quantity']
    v=(name, bprice,sprice,squantity)
    ins_product(v)
    return redirect ("/products")

@app.route("/sales")
def sales():
    # login_check()
    products= get_data("products")
    sales= get_data("sales")
    return render_template("sales.html", mysales=sales, myproducts=products)

@app.route("/add-sales", methods=["POST","get"])
def insert_sales():
    product_id= request.form["product_id"]
    quantity= request.form["quantity"]
    s= (product_id, quantity)
    insert_sale(s)
    return redirect ("/sales")


@app.route("/register", methods=["Post","get"])
def register():
    if request.method== "POST":
        full_name= request.form ["full_name"]
        email= request.form ["email"]
        password= request.form ["password"]
        create_users(full_name,email,password)
        

        if not check_email_exists(email):
            create_users(full_name,email,password)
            return redirect("/login")
        else:
            flash("email already exists")
            return redirect ("/login")
    return render_template("login.html")

    
@app.route("/login", methods=["Post","get"])
def login():
    # session['email']= request.form['email']
    # return render_template("/dashboard")
    
    if request.method== "POST":
        email= request.form ["email"]
        password= request.form["password"]
        user_id= email_password_match(email, password)

        if user_id:
            session["user_id"] = user_id
            return redirect ("/dashboard")
        else:
            flash("Login failed; username or password is not correct ")
    return render_template ("login.html")



@app.route("/logout")
def logout():
    session.pop("email")
    return redirect("/dashboard.html")


    


    
    


# @app.route("/insert_sale", methods=["Post"])
# def insert_sale():
#     pid= request.form['pid']
#     q= request.form['quantity']
#     time= request.form['created_at']
#     S=(pid,q, time)
#     insert_product(S)
#     return redirect ("/sales")

app.run(debug= True)
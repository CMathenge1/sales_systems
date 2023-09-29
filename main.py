from flask import Flask, render_template
from dbservice import get_data
from dbservice import insert_data
app=Flask(__name__)

@app.route("/")
def sales_system():
    return render_template("index.html")

@app.route("/dashboard")
def dashboad():
    return render_template("dashboard.html")

@app.route("/products")
def products():
    prods=get_data("products")
    return render_template("products.html", myproducts=prods)


@app.route("/sales")
def sales():
    sales= get_data("sales")
    return render_template("sales.html", mysales=sales)

app.run()
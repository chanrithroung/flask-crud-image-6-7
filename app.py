from flask import Flask, render_template, request, redirect, jsonify
import os
import db_connect
import uuid


app = Flask(__name__)


def upload_image(sourcefile=None):
    if sourcefile is not None:
        upload_dir = "static/uploads"
        _, ext = os.path.splitext( sourcefile.filename  )
        unique_filename =  str(uuid.uuid1()) + ext
        sourcefile.save( os.path.join(upload_dir, unique_filename))
    return unique_filename


@app.route("/")
def index():

    query =  "SELECT * FROM `products`"
    con = db_connect.db_connect()
    cursor = con.cursor()
    cursor.execute(query=query)

    products = cursor.fetchall()
    # return jsonify(products)

    return render_template("index.html", products=products)

@app.route("/create-product", methods=["GET","POST"])
def create_post():
    name= request.form['name']
    price = request.form['price']
    sourcefile = request.files['thumbnail']
    thumbnail = upload_image(sourcefile=sourcefile)


    query = f""" 
        INSERT INTO products( `product_name`, `product_price`, `thumbnail`) 
        VALUES ('{name}', '{price}', '{thumbnail}')
      """
    
    con = db_connect.db_connect()
    cursor = con.cursor()

    cursor.execute(query)
    con.commit()

    return redirect('/')

    



if __name__ == "__main__":
    app.run(debug=True)


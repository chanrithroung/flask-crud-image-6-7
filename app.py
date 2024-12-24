from flask import Flask, render_template, request
import os
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
    return render_template("index.html")

@app.route("/create-product", methods=["GET","POST"])
def create_post():
    sourcefile = request.files['thumbnail']
    return upload_image(sourcefile=sourcefile)



if __name__ == "__main__":
    app.run(debug=True)


from flask import Flask, render_template, jsonify
import json
import os 

app = Flask(__name__)

# giris sayfasi -> dashboard ->  reklamlar 
@app.route('/')
def get_all_posts():
   return render_template("index.html")

# ogretmen basvuru 
@app.route("/teacher_app")
def sentiment_garphic():
    return render_template("teacher_app.html")

@app.route("/student_app")
def number_of_comments():
    return render_template("student_app.html")

@app.route("/training_packages")
def brands():
    return render_template("training_packages.html")

@app.route("/about_train")
def contact():
    return render_template("about_train.html")

@app.route('/<brand>')
def brand_page(brand):
  
   return render_template('brand.html')



if __name__ == "__main__":
    app.run(debug=True)

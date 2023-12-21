from flask import Flask,render_template, request,redirect,url_for
from flask_mysqldb import MySQL
import random

app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'onlinelanguageeducation'
 
mysql = MySQL(app)
student_info = []
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "Login via the login Form"
     
    if request.method == 'POST':
        student_info.append(request.form['name'])
        student_info.append(request.form['last_name'])
        student_info.append(request.form['email'])

        return render_template("level_exam.html",student_info =student_info)

 
def generate_password():
    password = ''.join(random.choices('0123456789', k=4))
    return password

# def show_message_box(password):
#     messagebox.showinfo("Sifreniz: {password}", "Giris Yapabilmek icin bu sifreyi kaydetmeniz gerekmektedir.")

@app.route('/check_exam', methods=['POST'])
def check_exam():
    user_answers = []
    answers = ["3","3","2","2","1","2","1","1","1","1"]
    #for i in range(1,11):
        # question = "q" +str(i)
        # user_answers.append[request.form[question]]
    
    user_answers.append( request.form['q1'])
    user_answers.append( request.form['q2'])
    user_answers.append( request.form['q3'])
    user_answers.append( request.form['q4'])
    user_answers.append( request.form['q5'])
    user_answers.append( request.form['q6'])
    user_answers.append( request.form['q7'])
    user_answers.append( request.form['q8'])
    user_answers.append( request.form['q8'])
    user_answers.append( request.form['q10'])

    print(user_answers)

    score = 0
    for idx,answer in enumerate(user_answers):
        if answer == answers[idx]:
            score +=10 
    return save_exam_results(score)

@app.route('/check_student', methods=['POST'])
def check_student():
    # Formdan gelen e-posta ve şifre bilgilerini al
    email = request.form['email']
    password = request.form['password']

    # Veritabanında sorgu yapılacak tablonun adı
    table_name = 'students' 

    # Veritabanında bu e-posta ve şifre ile öğrenci var mı kontrol et
    cursor = mysql.connection.cursor()
    # query = f"SELECT * FROM {table_name} WHERE email = %s AND password = %s"
    # query = f"SELECT name FROM students WHERE email = {email} AND password = {password};"
    cursor.execute("SELECT * FROM students WHERE email = %s AND password = %s", (email, password))
    
    student = cursor.fetchone()
    cursor.close()

    print("hello")

    if student:
        # Eğer öğrenci varsa, öğrenci sayfasına yönlendir
        return render_template("student.html")
    else:
        # Eğer öğrenci yoksa, hata mesajı göster veya başka bir işlem yap
        return render_template('student_app.html', message='Öğrenci bulunamadı.')

def save_exam_results(score):
    score = str(score)
    cursor = mysql.connection.cursor()
    cursor.execute(''' INSERT INTO exam_results (name,last_name,email,score) VALUES (%s,%s,%s,%s)''',(student_info[0],student_info[1],student_info[2],score))
    mysql.connection.commit()
    cursor.execute('SELECT LAST_INSERT_ID()')
    student_id = cursor.fetchone()[0]
    cursor.close() 
    student_info.append(student_id)
    return get_packages(score)

def get_packages(score):
    try:
        cursor = mysql.connection.cursor()
        query = f"SELECT package, info, price FROM level_and_packages WHERE level = {score};"
        cursor.execute(query)
        result = cursor.fetchone()

        if result:
            package, info, price = result
            return choose_package(package, info, price )
        else:
            return "Level not found in the database."

    except Exception as e:
        return f"An error occurred: {str(e)}"

    finally:
        cursor.close()

package_info  = ""
def choose_package( package, info, price ):

    package_info = package
    return render_template("package.html",title = package, info = info,price = price)

@app.route('/save_student', methods=['POST'])
def save_student(password):
    cursor = mysql.connection.cursor()
    cursor.execute(''' INSERT INTO students (id,name,last_name,email,package,password) VALUES (%s,%s,%s,%s,%s,%s)''',(student_info[3],student_info[0],student_info[1],student_info[2],package_info,password))
    mysql.connection.commit()
    cursor.close()
    # return show_message_box(password)  -> cok yavas calısıyor
    return password
# giris sayfasi -> dashboard ->  reklamlar

@app.route('/accounter_page', methods=['POST'])
def accounter_page():
    return render_template("accounter.html")

@app.route('/accounter', methods=['POST'])
def accounter():
    #odeme bilgileri kontrol 
    password = generate_password()
    return save_student(password)
     

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

@app.route("/teacher_app")
def number_of_comments():
    return render_template("student_app.html")

@app.route("/login_student")
def login_student():
    return render_template("login_student.html")

@app.route("/training_packages")
def brands():
    return render_template("training_packages.html")

@app.route("/about_train")
def contact():
    return render_template("about_train.html")
if __name__ == "__main__":
    app.run(debug=True)

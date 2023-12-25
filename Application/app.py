from flask import Flask,render_template, request,redirect,url_for
from flask_mysqldb import MySQL
import random
from datetime import datetime


app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'onlinelanguageeducation'
 

mysql = MySQL(app)
student_info = []
teacher_info = []
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "Login via the login Form"
     
    if request.method == 'POST':
        student_info.append(request.form['name'])
        student_info.append(request.form['last_name'])
        student_info.append(request.form['email'])

        return render_template("level_exam.html",student_info =student_info)

@app.route('/sign_teacher', methods = ['POST', 'GET'])
def sign_teacher():
    if request.method == 'GET':
        return "Login via the login Form"
     
    if request.method == 'POST':
        teacher_info.append(request.form['name'])
        teacher_info.append(request.form['last_name'])
        teacher_info.append(request.form['email'])

        return render_template("level_exam_teacher.html",teacher_info =teacher_info)


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

@app.route('/check_exam_teacher', methods=['POST'])
def check_exam_teacher():
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
    return save_teacher_apply(score)


def save_teacher_apply(score):
    score = str(score)
    cursor = mysql.connection.cursor()
    cursor.execute(''' INSERT INTO teacher_apply (name,last_name,email,score,state) VALUES (%s,%s,%s,%s,%s)''',(teacher_info[0],teacher_info[1],teacher_info[2],score,"1"))
    mysql.connection.commit()
    cursor.execute('SELECT LAST_INSERT_ID()')
    teacher_id = cursor.fetchone()[0]
    cursor.close() 
    teacher_info.append(teacher_id)
    return "Yanitiniz Kaydedildi"

@app.route('/coordinator', methods=['POST'])
def coordinator():
    cursor = mysql.connection.cursor()

    ev =1
    cursor.execute('''SELECT * FROM teacher_apply WHERE state = %s''', (ev))
    teacher_apply = cursor.fetchone()
    cursor.close()
    print(teacher_apply)
    render_template("display_teacher_apply.html",teacher = teacher_apply)


    

@app.route('/check_coordinator', methods=['POST'])
def check_coordinator():
    email = request.form['email']
    password = request.form['password']
    print("hello")
    if email == "bculture@gmail.com" and password == "1881":

        cursor = mysql.connection.cursor()

        ev ="1"
        cursor.execute('''SELECT * FROM teacher_apply WHERE state = %s''', (ev))
        teacher_apply = cursor.fetchmany(size=5) 
        # cursor.execute('''SELECT * FROM teacher_apply''')
        
        cursor.close()
        print(teacher_apply)
        return render_template("display_teacher_apply.html", teachers=teacher_apply)
    else:
        return render_template("index.html")

student_level = ""
user_password = ""
user_email = ""
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
    cursor.execute("SELECT package,password,email FROM students WHERE email = %s AND password = %s", (email, password))
    
    student = cursor.fetchone()
    cursor.close()

    print("hello")

    if student:
        # Eğer öğrenci varsa, öğrenci sayfasına yönlendir
        global student_level
        global user_password
        global user_email
        student_level,user_password,user_email = student
        
        now = datetime.now()
        now_month = now.month
        now_day = now.day

        if now_month % 3 == 0 and now_day == 15:
            
            return check_levels()
        else:
            return render_template("student.html")
    else:
        # Eğer öğrenci yoksa, hata mesajı göster veya başka bir işlem yap
        return render_template('student_app.html', message='Öğrenci bulunamadı.')

@app.route('/check_teacher', methods=['POST'])
def check_teacher():
    # Formdan gelen e-posta ve şifre bilgilerini al
    email = request.form['email']
    password = request.form['password']

    # Veritabanında sorgu yapılacak tablonun adı
    table_name = 'students' 

    # Veritabanında bu e-posta ve şifre ile öğrenci var mı kontrol et
    cursor = mysql.connection.cursor()
    # query = f"SELECT * FROM {table_name} WHERE email = %s AND password = %s"
    # query = f"SELECT name FROM students WHERE email = {email} AND password = {password};"
    cursor.execute("SELECT password,email FROM teachers WHERE email = %s AND password = %s", (email, password))
    
    student = cursor.fetchone()
    
    cursor.close()

    print("hello")

    if student:
    
        # Eğer öğrenci varsa, öğrenci sayfasına yönlendir
        global student_level
        global user_password
        global user_email
        user_password,user_email = student
        return render_template("teacher.html")
    else:
        # Eğer öğrenci yoksa, hata mesajı göster veya başka bir işlem yap
        return render_template('teacher_app.html', message='Öğretmen bulunamadı.')

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
    global package_info
    package_info = package
    print(package_info)
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

@app.route('/accept_to_teacher' , methods = ["post","get"])
def accept_to_teacher():
    # teacher_id = request.form['teacher_id']
    name = request.form['name']
    last_name = request.form['last_name']
    email = request.form['email']
    level = request.form['level']
    print(id,name,last_name,email,level)
    return save_teacher(id,name,last_name,email,level)
    

def save_teacher(id,name,last_name,email,level):
    password = generate_password()
    cursor = mysql.connection.cursor()
    cursor.execute(''' INSERT INTO teachers (name,last_name,email,level,password) VALUES (%s,%s,%s,%s,%s)''',(name,last_name,email,level,password))
    mysql.connection.commit()
    cursor.close()
    # return show_message_box(password)  -> cok yavas calısıyor
    return password


# @app.route("/teacher_app")
# def number_of_comments():
#     return render_template("student_app.html")

@app.route("/login_student")
def login_student():
    return render_template("login_student.html")

@app.route("/login_teacher")
def login_teacher():
    return render_template("login_teacher.html")

@app.route("/login_coordinator")
def login_coordinator():
    return render_template("login_coordinator.html")

@app.route("/training_packages")
def brands():
    return render_template("training_packages.html")

@app.route("/about_train")
def contact():
    return render_template("about_train.html")


@app.route("/upload_source" , methods = ["post","get"])
def upload_source():
    return render_template("upload_source.html")

@app.route('/save_source' , methods = ["post","get"])
def save_source():
    name = request.form['name']
    link = request.form['link']
    level = request.form['level']

    cursor = mysql.connection.cursor()
    cursor.execute(''' INSERT INTO sources (name,link,level) VALUES (%s,%s,%s)''',(name,link,level))
    mysql.connection.commit()
    cursor.close() 
    return "Kaydedildi"

@app.route('/view_source' , methods = ["post","get"])
def view_source():
    try:
        global student_level
        print(student_level)
        if(student_level == "A1"):
            student_level = "1"
        elif(student_level == "A2"):
            student_level = "2"
        elif(student_level == "B1"):
            student_level = "3"
        elif(student_level == "B2"):
            student_level = "4"
        elif(student_level == "C1"):
            student_level = "5"
        elif(student_level == "C2"):
            student_level = "6"
        else:
            student_level = "0"
        cursor = mysql.connection.cursor()
        cursor.execute('''SELECT name,link FROM sources WHERE level = %s''', (student_level))
        
        sources = cursor.fetchmany(size=1)
        
        cursor.close()
        print(sources)
        if sources:
            return render_template("view_sources.html", sources=sources)
        else:
            return "Level not found in the database."

    except Exception as e:
        return f"An error occurred: {str(e)}"

@app.route('/send_message' , methods = ["post","get"])
def send_message():
    return render_template("write_message.html")

@app.route('/save_message' , methods = ["post","get"])
def save_message():
    message = request.form['message']
    email = request.form['email']
    cursor = mysql.connection.cursor()
    cursor.execute(''' INSERT INTO messages (message,email,from_email) VALUES (%s,%s,%s)''',(message,email,user_email))
    mysql.connection.commit()
    cursor.close()
    # return show_message_box(password)  -> cok yavas calısıyor
    return "Mesaj Gonderildi"
    

@app.route('/view_messages' , methods = ["post","get"])
def view_messages():
    global user_email
    email = user_email
    print(user_email)
    print(email)
    print(type(email))
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT message,from_email FROM messages WHERE email = %s ",  (user_email,))
    
    messages = cursor.fetchone()
    
    print(messages)
    mysql.connection.commit()
    cursor.close()
    # return show_message_box(password)  -> cok yavas calısıyor
    return render_template("view_messages.html",messages= messages)
    

# TEACHER
@app.route("/upload_video" , methods = ["post","get"])
def upload_video():
    return render_template("upload_video.html")

@app.route('/save_video' , methods = ["post","get"])
def save_video():
    name = request.form['name']
    link = request.form['link']
    level = request.form['level']

    cursor = mysql.connection.cursor()
    cursor.execute(''' INSERT INTO videos (name,link,level) VALUES (%s,%s,%s)''',(name,link,level))
    mysql.connection.commit()
    cursor.close() 
    return "Kaydedildi"

@app.route('/watch_video' , methods = ["post","get"])
def watch_video():
    try:
        global student_level
        print(student_level)
        
        cursor = mysql.connection.cursor()
        cursor.execute('''SELECT name,link FROM videos WHERE level = %s''', (student_level,))
        
        sources = cursor.fetchmany(size=3)
        
        cursor.close()
        print(sources)
        if sources:
            return render_template("watch_video.html", sources=sources)
        else:
            return "Level not found in the database."

    except Exception as e:
        return f"An error occurred: {str(e)}"

# HOMEWORK
@app.route('/give_homework' , methods = ["post","get"])
def give_homework():
    return render_template("give_homework.html")

@app.route('/save_homework' , methods = ["post","get"])
def save_homework():
    homework = request.form['homework']
    email = request.form['email']
    cursor = mysql.connection.cursor()
    cursor.execute(''' INSERT INTO homeworks (homework,email,from_email) VALUES (%s,%s,%s)''',(homework,email,user_email))
    mysql.connection.commit()
    cursor.close()
    # return show_message_box(password)  -> cok yavas calısıyor
    return "Odev Gonderildi"
    

@app.route('/display_homework' , methods = ["post","get"])
def display_homework():
    global user_email
    email = user_email
    print(user_email)
    print(email)
    print(type(email))
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT id,homework FROM homeworks WHERE email = %s ",  (user_email,))
    
    messages = cursor.fetchone()
    
    print(messages)
    mysql.connection.commit()
    cursor.close()
    # return show_message_box(password)  -> cok yavas calısıyor
    return render_template("display_homework.html",messages= messages)

@app.route('/send_answer' , methods = ["post","get"]) 
def send_answer():
    if request.method == 'POST':
        answer = request.form['answer']
        id = request.form['odev_id']
        # Veritabanına bağlan
        cursor = mysql.connection.cursor()

        try:
            # Belirli ID'ye sahip satırın "answer" sütununu güncelle
            update_query = "UPDATE homeworks SET answer = %s WHERE id = %s"
            cursor.execute(update_query, (answer, id))

            # Değişiklikleri kaydet
            mysql.connection.commit()

            return "Cevap başarıyla güncellendi."

        except Exception as e:
            # Hata durumunda geri dön
            return f'Hata: {str(e)}'

        finally:
            # Cursor ve bağlantıyı kapat
            cursor.close()

    return render_template("update_answer.html")

@app.route('/view_homework' , methods = ["post","get"])
def view_homework():
    global user_email
    email = user_email
    print(user_email)
    print(email)
    print(type(email))
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT id,homework,answer FROM homeworks WHERE from_email = %s ",  (user_email,))
    
    messages = cursor.fetchone()
    
    print(messages)
    mysql.connection.commit()
    cursor.close()
    # return show_message_box(password)  -> cok yavas calısıyor
    return render_template("view_homework.html",messages= messages)

@app.route('/send_score' , methods = ["post","get"]) 
def send_score():
    if request.method == 'POST':
        score = request.form['odev_score']
        id = request.form['odev_id']
        # Veritabanına bağlan
        cursor = mysql.connection.cursor()

        try:
            # Belirli ID'ye sahip satırın "answer" sütununu güncelle
            update_query = "UPDATE homeworks SET score = %s WHERE id = %s"
            cursor.execute(update_query, (score, id))

            # Değişiklikleri kaydet
            mysql.connection.commit()

            return "Puan kaydedildi."

        except Exception as e:
            # Hata durumunda geri dön
            return f'Hata: {str(e)}'

        finally:
            # Cursor ve bağlantıyı kapat
            cursor.close()

    return render_template("update_answer.html")

@app.route("/start_class" , methods = ["post","get"])
def start_class():
    return render_template("start_class.html")
    
@app.route('/save_class' , methods = ["post","get"])
def save_class():
    name = request.form['name']
    link = request.form['link']
    time = request.form['time']
    email = request.form['email']
    cursor = mysql.connection.cursor()
    cursor.execute(''' INSERT INTO classes (name,link,email,time) VALUES (%s,%s,%s,%s)''',(name,link,email,time))
    mysql.connection.commit()
    cursor.close() 
    return "Kaydedildi"

@app.route('/attend_class' , methods = ["post","get"])
def attend_class():
    global user_email
    email = user_email
    print(user_email)
    print(email)
    print(type(email))
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT id,time,link FROM classes WHERE email = %s ",  (user_email,))
    
    messages = cursor.fetchone()
    
    print(messages)
    mysql.connection.commit()
    cursor.close()
    # return show_message_box(password)  -> cok yavas calısıyor
    return render_template("attend_class.html",messages= messages)


@app.route('/attended_class' , methods = ["post","get"]) 
def attended_class():
    if request.method == 'POST':

        id = request.form['ders_id']
        # Veritabanına bağlan
        
        cursor = mysql.connection.cursor()
        
        try:
            # Belirli ID'ye sahip satırın "answer" sütununu güncelle
            update_query = "UPDATE classes SET state = %s WHERE id = %s"
            cursor.execute(update_query, ("1", id))

            # Değişiklikleri kaydet
            mysql.connection.commit()

            return "Derse katılındı."

        except Exception as e:
            # Hata durumunda geri dön
            return f'Hata: {str(e)}'

        finally:
            # Cursor ve bağlantıyı kapat
            cursor.close()

    return render_template("attend_class.html")

# SPEAKİNG CLUB-> seviyey gore ders atama 
   
@app.route("/start_club" , methods = ["post","get"])
def start_club():
    return render_template("start_club.html")
    
@app.route('/save_club' , methods = ["post","get"])
def save_club():
    name = request.form['name']
    link = request.form['link']
    time = request.form['time']
    level = request.form['level']
    cursor = mysql.connection.cursor()
    cursor.execute(''' INSERT INTO clubs (name,link,level,time) VALUES (%s,%s,%s,%s)''',(name,link,level,time))
    mysql.connection.commit()
    cursor.close() 
    return "Kaydedildi"

@app.route('/attend_club' , methods = ["post","get"])
def attend_club():
    global student_level
    print(student_level)
    if(student_level == "A1"):
        student_level = "1"
    elif(student_level == "A2"):
        student_level = "2"
    elif(student_level == "B1"):
        student_level = "3"
    elif(student_level == "B2"):
        student_level = "4"
    elif(student_level == "C1"):
        student_level = "5"
    elif(student_level == "C2"):
        student_level = "6"
    else:
        student_level = "0"
    print(user_email)

    cursor = mysql.connection.cursor()
    cursor.execute("SELECT name,time,link FROM clubs WHERE level = %s ",  (student_level,))
    
    messages = cursor.fetchone()
    
    print(messages)
    mysql.connection.commit()
    cursor.close()
    # return show_message_box(password)  -> cok yavas calısıyor
    return render_template("attend_club.html",messages= messages)

# KONTROL SİSTEMİ ->coordinator sisteme giris yapinca calisacak
def check_levels():
    try:
    # Veritabanına bağlan
        cursor = mysql.connection.cursor()

        # Aynı e-posta adresine sahip kullanıcıların score değerlerini topla ve ortalamasını al
        query = "SELECT AVG(score) FROM homeworks WHERE email = %s"
        cursor.execute(query, (user_email,))

        # Ortalamayı al ve sonucu getir
        ortalama_score = cursor.fetchone()[0]

        query = "SELECT package FROM students WHERE email = %s"
        cursor.execute(query, (user_email,))

        # Ortalamayı al ve sonucu getir
        package = cursor.fetchone()[0]

        if package == "A1":
            new_package = "A2"
        elif package == "A2":
            new_package = "B1"
        elif package == "B1":
            new_package = "B2"
        elif package == "B2":
            new_package = "C1"
        elif package == "C1":
            new_package = "C2"
        else:
            new_package = "A1"
          

        if ortalama_score >= 70:
            update_query = "UPDATE students SET package = %s WHERE email = %s"
            cursor.execute(update_query, (new_package, user_email))

            # Değişiklikleri kaydet
            mysql.connection.commit()
            
        return render_template("success.html", ortalama_score=ortalama_score)

    except Exception as e:
        # Hata durumunda geri dön
        return f'Hata: {str(e)}'

    finally:
        # Cursor ve bağlantıyı kapat
        cursor.close()
    # Koordinator

if __name__ == "__main__":
    app.run(debug=True)


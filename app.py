from flask import Flask,render_template,redirect,url_for,session,request
from datetime import datetime
from form import AddForm,InsertForm,Delete_form,UpdateForm
import psycopg2

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Crudoperations'

### Table Created ###
def table():
    conn = psycopg2.connect(database = 'postgres',
                            port = '5432',
                            user = 'postgres',
                            password = 'root',
                            host = 'localhost')
    cursor = conn.cursor()

    sql = ('''create table if not exists Student(
           id SERIAL PRIMARY KEY,
           first_name varchar(20) NOT NULL,
           last_name varchar(20) NOT NULL,
           std_class varchar(20) NOT NULL,
           date varchar NOT NULL);''')
    
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()

### ADD Data ###
def add_values(entry):
        conn = psycopg2.connect(database = 'postgres',
                                host = 'localhost',
                                user = 'postgres',
                                password = 'root',
                                port = '5432')
        
        cursor = conn.cursor()
        
        sql = ('''insert into Student (first_name,last_name,std_class,date) \
               values (%s,%s,%s,%s)''')
        for data in entry:
            cursor.execute(sql,data)
        conn.commit()
        cursor.close()
        conn.close()

### Fetch Data ###
def fetch_data():
    conn = psycopg2.connect(database = 'postgres',
                                host = 'localhost',
                                user = 'postgres',
                                password = 'root',
                                port = '5432')
        
    cursor = conn.cursor()
    
    sql = ('''select * from student''')
    cursor.execute(sql)
    data = cursor.fetchall()
    return data

### fetch single Row Data ###
def fetchone_data(id):
    conn = psycopg2.connect(database = 'postgres',
                                host = 'localhost',
                                user = 'postgres',
                                password = 'root',
                                port = '5432')
        
    cursor = conn.cursor()
    
    sql = ('''select * from student where id=%s''')
    cursor.execute(sql,(id,))
    data = cursor.fetchall()
    return data

### Delete Data ###
def delete_record(id):
    try:
        conn = psycopg2.connect(database = 'postgres',
                                    host = 'localhost',
                                    user = 'postgres',
                                    password = 'root',
                                    port = '5432')
            
        cursor = conn.cursor()
        sql = ('delete from student where id=%s')
        cursor.execute(sql,(id,))
        print('Executed Query')
        conn.commit()
        conn.close()
        return (f'The data of id={id} is deleted')
    except(psycopg2.Error) as e:
        print(e)

### Update Data ###
def Update_data(entry):
    conn = psycopg2.connect(database = 'postgres',
                            host = 'localhost',
                            user = 'postgres',
                            password = 'root',
                            port = '5432')
            
    cursor = conn.cursor()
    sql = ('''UPDATE student SET first_name=%s,last_name=%s, std_class=%s WHERE id=%s''' )
    for dt in entry:
        cursor.execute(sql,dt)
    conn.commit()

@app.route('/',methods=['GET','POST'])
def home():
    table()
    form = AddForm()

    if form.validate_on_submit():
        return redirect(url_for('add'))
    
    data = fetch_data()
    
    return render_template('home.html',form=form,data=data)

@app.route('/New_Student',methods=['GET','POST'])
def add():
    form = InsertForm()
    if form.validate_on_submit():

        first_name = form.first_name.data
        last_name = form.last_name.data
        std_class = form.std_class.data
        date = datetime.today()

        print(first_name,last_name,std_class,date)
        entry = [(first_name,last_name,std_class,date)]

        add_values(entry)   

        return redirect(url_for('home'))
    return render_template('add.html',form=form)

@app.route('/delete',methods=['GET','POST'])
def delete():

    id = request.form.get('id')
    form = Delete_form()
    if form.validate_on_submit():
        ids = request.form.get('id')
        data_id = (int(ids))
        delete_record(data_id)
        return redirect(url_for('home'))

    return render_template('delete.html',form=form,id=id)

@app.route('/Updata_Data',methods=['GET','POST'])
def update():

    id = request.form.get('id')
    data = fetchone_data(id)

    form = UpdateForm()
    if form.validate_on_submit():
        id = form.id.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        std_class = form.std_class.data

        entry = [(first_name,last_name,std_class,id)]
        
        Update_data(entry)

        return redirect(url_for('home'))
    return render_template('edit.html',form=form,data=data)

if __name__ == "__main__":
    app.run(debug=True)

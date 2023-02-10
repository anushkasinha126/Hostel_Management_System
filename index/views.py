from django.shortcuts import render
from flask import Flask, render_template, request, redirect
from django.conf import settings
from django.conf.urls.static import static
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

# my db connection
local_server=True
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:@localhost/hms'
db=SQLAlchemy(app)


class Contact(db.Model):
    srno = db.Column(db.Integer, primary_key=True)
    cname = db.Column(db.String, nullable=False )
    cemail = db.Column(db.String,unique=True, nullable=False)
    cphone = db.Column(db.Integer, nullable=False)
    query = db.Column(db.String, nullable=False)

#srno, cname, cemail, cphone, query
class Admin(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False )
    password = db.Column(db.String, nullable=False)

#srno	sname	usn	roomno	email	phone	address	dob	pname	pphone	
class Student(db.Model):
    srno = db.Column(db.Integer, primary_key=True)
    sname = db.Column(db.String, nullable=False)
    usn = db.Column(db.String, unique=True, nullable=False)
    amount = db.Column(db.Integer, nullable=True)
    roomno = db.Column(db.Integer, nullable=False )
    email = db.Column(db.String,unique=True, nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String, nullable=False )
    dob = db.Column(db.String, nullable=False)
    pname = db.Column(db.String, nullable=False)
    pphone= db.Column(db.Integer, nullable=False )

#srno	eid	ename	ephone	address	designation	
class Employee(db.Model):
    srno = db.Column(db.Integer, primary_key=True)
    ename= db.Column(db.String, nullable=False)
    ephone = db.Column(db.Integer, nullable=False)
    address= db.Column(db.String, nullable=False)
    designation= db.Column(db.String, nullable=False)

class Room(db.Model):
    roomno = db.Column(db.Integer, primary_key=True)
    type= db.Column(db.String, nullable=False)
    # status= db.Column(db.String, nullable=False)
    occ_bed= db.Column(db.Integer, nullable=True)

class Trigr(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    roomno= db.Column(db.Integer, nullable=False)
    usn = db.Column(db.String, nullable=False)
    Action= db.Column(db.String, nullable=False)
    date= db.Column(db.String, nullable=False)

class vacRoom(db.Model):
    roomno = db.Column(db.Integer, primary_key=True)
    type= db.Column(db.String, nullable=False)
    # status= db.Column(db.String, nullable=False)
    occ_bed= db.Column(db.Integer, nullable=False)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/adminred")
def adminred():
    return render_template('adminred.html')

# @app.route("/test")
# def test():
#     return render_template('.html')

@app.route("/room")
def room():
    return render_template('room.html')

@app.route("/admin", methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        username=request.form.get('username')
        password=request.form.get('password')
        user=Admin.query.filter_by(username=username, password=password).first()
        if user:
            return render_template('adminred.html')
    return render_template('admin.html')

@app.route("/sdetails", methods=['GET', 'POST'])
def sdetails():
    student=Student.query.all()
    return render_template('studetails.html', student=student)

@app.route("/edetails", methods=['GET', 'POST'])
def edetails():
    emp=Employee.query.all()
    return render_template('edetails.html', emp=emp)

@app.route("/rdetails", methods=['GET', 'POST'])
def rdetails():
    room=Room.query.all()
    return render_template('rdetails.html', room=room)

@app.route("/regdetails")
def regdetails():
    trigr=Trigr.query.all()
    return render_template('trigr.html', trigr=trigr)

    
@app.route("/vacroom")
def vacroom():
    vacroom=vacRoom.query.all()
    return render_template('vacroom.html', vacroom=vacroom)
    
@app.route("/delete/<string:srno>", methods=['GET', 'POST'])
def delete(srno):
    student=Student.query.filter_by(srno=srno).first()
    db.session.delete(student)
    db.session.commit()
    return redirect('/sdetails')

@app.route("/delete1/<string:srno>", methods=['GET', 'POST'])
def delete1(srno):
    emp=Employee.query.filter_by(srno=srno).first()
    db.session.delete(emp)
    db.session.commit()
    return redirect('/edetails')
    

@app.route("/delete2/<string:srno>", methods=['GET', 'POST'])
def delete2(roomno):
    roomno=Room.query.filter_by(roomno=roomno).first()
    db.session.delete(room)
    db.session.commit()
    return redirect('/rdetails')
    
@app.route("/student", methods=['GET', 'POST'])
def student():
    if request.method == 'POST':
        name=request.form.get('name')
        usn=request.form.get('usn')
        amt=request.form.get('amt')
        room=request.form.get('room')
        email=request.form.get('email')
        PhoneNumber_countrycode=request.form.get('PhoneNumber_countrycode')
        address=request.form.get('address')
        Date=request.form.get('Date')
        pname=request.form.get('pname')
        PhoneNumber1_countrycode=request.form.get('PhoneNumber1_countrycode')

        entry=Student(sname=name, usn=usn, amount=amt, roomno=room, email=email, phone=PhoneNumber_countrycode, address=address, dob=Date, pname=pname, pphone=PhoneNumber1_countrycode)
        db.session.add(entry)
        db.session.commit()
        return render_template('msg1.html')
    return render_template('student.html')
#srno	sname	usn	roomno	email	phone	address	dob	pname	pphone	

@app.route("/emp", methods=['GET', 'POST'])
def emp():
    if request.method == 'POST':
        name=request.form.get('name')
        PhoneNumber_countrycode=request.form.get('PhoneNumber_countrycode')
        address=request.form.get('address')
        desig=request.form.get('desig')

        entry=Employee( ename=name, ephone=PhoneNumber_countrycode, address=address, designation=desig)
        db.session.add(entry)
        db.session.commit()
        return render_template('msg1.html')
    return render_template('emp.html')
#srno	ename	ephone	address	designation

@app.route("/contact",methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        name=request.form.get('name')
        email=request.form.get('email')
        phone=request.form.get('phone')
        query=request.form.get('query')

        entry=Contact( cname=name, cemail=email, cphone=phone, query=query)
        db.session.add(entry)
        db.session.commit()
        return render_template('msg.html')
    return render_template('contact.html')

app.run(debug=True)
# Create your views here.

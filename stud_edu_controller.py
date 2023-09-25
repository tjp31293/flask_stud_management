from student_info import *
from flask import render_template,request
from sqlalchemy.sql import exists

@app.route('/', methods=['GET'])
def start_view():
    return render_template('login.html')


@app.route('/stud/sign_in', methods=['POST'])
def user_login():
    error = ''
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username and password:
            if username == 'viraj' and password == 'abc':

                return render_template('home.html')
            else:
                error = 'Invalid...|'
        else:
            error = 'Username and password can not be blank|'

    return render_template('login.html', error=error)

@app.route('/stud/sign_up',methods=['GET'])
def user_sign_up():
    return  render_template('view.html')

@app.route('/stud/add',methods=['POST'])
def stud_add():
    if request.method == 'POST':
        formdata = request.form
        if formdata:
            # Add the student
            stdid     = formdata.get('id')

            stdname   = formdata.get('name')
            stdgender = formdata.get('gender')
            stdbirth  = formdata.get('birthday')

            bloodgroup= formdata.get('bloodgroup')
            fname     = formdata.get('fname')
            phoneno   = formdata.get('phoneno')
            occupation= formdata.get('occcupation')
            email_id  = formdata.get('emailId')
            address   = formdata.get('address')
            username = formdata.get('username')


            password  = formdata.get('password')
            #stdrecord = stud_personal_info.query.filter_by(password=password).first()

            exists = db.session.query(
                db.session.query(stud_personal_info).filter_by(password=password).exists()
            ).scalar()

            if exists:
                return render_template('view.html', msg='Password already exists..Please change the password')
            else:
                stud = stud_personal_info(name=stdname,gender=stdgender,
                                  birth_date=stdbirth,blood_group=bloodgroup,fname=fname,mobileno=phoneno,
                                  occupation=occupation,email_id=email_id,address=address,
                                  username=username,password=password)


                db.session.add(stud)

                db.session.commit()

                stud_tenth_marks = formdata.get('marks')
                stud_grade = formdata.get('grade')
                stud_subject = formdata.getlist('subject')
                selected = ''
                for item in stud_subject:
                    selected = selected + item + ","
                stud_edu = stud_educational_info(stud_tenth_marks=stud_tenth_marks,edu_stud_id =stud.id,
                                                stud_grade=stud_grade,stud_subject=selected)



                db.session.add(stud_edu)
                db.session.commit()

                return  render_template('view.html',msg='Record added successufully')

@app.route('/stud/sign_in',methods=['POST'])
def stud_sign_in():
    if request.method == 'POST':
        formdata = request.form







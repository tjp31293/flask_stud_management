from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/stud_edu_db'
app.config['SECRET_KEY']  = "182KSK91023198jsds7878402940954*&*$@"
db = SQLAlchemy(app)
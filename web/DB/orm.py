from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request
from .db_info import user_name, pw, host_name, database_name


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{user_name}:{pw}@{host_name}/{database_name}'
db = SQLAlchemy(app)


# User 모델 클래스 정의
class User(db.Model):
    idx = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text, nullable=False, unique=True)
    name = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable=False)
    birth = db.Column(db.TIMESTAMP, nullable=False)
    phone_number = db.Column(db.Text, nullable=False)
    img = db.Column(db.LargeBinary)

    def verify_login(self, password):
        return self.password == password

# Supervisor 모델 클래스 정의
class Supervisor(db.Model):
    idx = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text, nullable=False, unique=True)
    name = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable=False)
    birth = db.Column(db.TIMESTAMP, nullable=False)
    phone_number = db.Column(db.Text, nullable=False)
    sns_id = db.Column(db.Text)

    def verify_login(self, password):
        return self.password == password

# User 테이블에 데이터 추가하는 뷰 함수
@app.route('/add_user', methods=['POST'])
def add_user():
    # HTML 폼에서 입력한 데이터 받아오기
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    birth = request.form.get('birth')
    phone_number = request.form.get('phone_number')

    # 이미 존재하는 이메일인지 확인
    if User.query.filter_by(email=email).first():
        return 'Email already exists!'

    # User 테이블에 데이터 추가
    user = User(email=email, name=name, password=password, birth=birth, phone_number=phone_number)
    db.session.add(user)
    db.session.commit()

    return 'User added successfully!'

# Supervisor 테이블에 데이터 추가하는 뷰 함수
@app.route('/add_supervisor', methods=['POST'])
def add_supervisor():
    # HTML 폼에서 입력한 데이터 받아오기
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    birth = request.form.get('birth')
    phone_number = request.form.get('phone_number')
    sns_id = request.form.get('sns_id')

    # 이미 존재하는 이메일인지 확인
    if Supervisor.query.filter_by(email=email).first():
        return 'Email already exists!'

    # Supervisor 테이블에 데이터 추가
    supervisor = Supervisor(email=email, name=name, password=password, birth=birth, phone_number=phone_number, sns_id=sns_id)
    db.session.add(supervisor)
    db.session.commit()

    return 'Supervisor added successfully!'

# 로그인 체크하는 뷰 함수
@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()
    supervisor = Supervisor.query.filter_by(email=email).first()

    if user:
        if user.verify_login(password):
            return 'User login successful!'
        else:
            return 'Incorrect password!'
    elif supervisor:
        if supervisor.verify_login(password):
            return 'Supervisor login successful!'
        else:
            return 'Incorrect password!'
    else:
        return 'User or Supervisor does not exist!'

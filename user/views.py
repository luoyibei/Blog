from flask import Blueprint,session,render_template,abort
from flask import render_template,request,redirect
from user.models import User
from lib.orm import db

user_bp = Blueprint('user',__name__,url_prefix='/user')
user_bp.template_folder = './templates'


@user_bp.route('/',methods=('POST','GET'))
def login():
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        try:
            user = User.query.filter_by(username = name).one()
        except:
            db.session.rollback()
            return '用户昵称错误'
        # if not user:
        #     return '无此用户'
        if user.password != password:
            return '密码错误！'
        session['name'] = name
        return redirect('/user/index')
    else:
        return render_template('login.html')


@user_bp.route('/index')
def index():
    name = session.get('name')
    user = User.query.filter_by(username = name).one()
    if user.username == session.get('name'):
        return '123'
        # return render_template('demo.html', user=user)
    else:
        abort(404)


@user_bp.route('/register',methods=('POST','GET'))
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        city = request.form.get('city')
        user = User(username=name,password=password,city=city)
        db.session.add(user)
        db.session.commit()
        #
        # session['name'] = name
        return redirect('/user/')
    else:
        return render_template('register.html')
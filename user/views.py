from flask import Blueprint,session
from flask import render_template,request,redirect
from user.models import User
from lib.orm import db

user_bp = Blueprint('user',__name__,url_prefix='/user')
user_bp.template_folder = './templates'


@user_bp.route('/login',methods=('POST','GET'))
def user_login():
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
        return redirect('/blog/home?username=%s' % user.username)
    else:
        return render_template('login.html')

#
# @user_bp.route('/index')
# def index():
#     name = session.get('name')
#     user = User.query.filter_by(username = name).one()
#     if user.username == session.get('name'):
#         session['name'] = name
#         # return '123'
#
#         return render_template('blog_home.html', user=user)


@user_bp.route('/register',methods=('POST','GET'))
def user_register():
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        city = request.form.get('city')
        user = User(username=name,password=password,city=city)
        db.session.add(user)
        db.session.commit()
        return redirect('/user/login')
    else:
        return render_template('register.html')


@user_bp.route('/h')
def h():
    return render_template('login.html')
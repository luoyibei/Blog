from flask import Flask
from flask import  redirect,request,session
from flask import render_template
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
import pymysql

from user import models
from blog.views import blog_bp
from lib.orm import db
from user.views import user_bp
from user.models import User


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:19971231@127.0.0.1/Blog"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
manager = Manager(app)
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)
app.secret_key = r'vdchjgoihe$#%$T^786653*(\btior'
db.init_app(app)


@manager.command
def add_data():
    '''添加初始数据'''
    u1 = User(username='Tom', password='123',city='北京')
    u2 = User(username='Lucy', password='123',city='上海')
    u3 = User(username='Jerry', password='123',city='广州')
    u4 = User(username='Jack', password='123',city='广州')

    db.session.add_all([u1,u2,u3,u4])
    db.session.commit()


app.register_blueprint(user_bp)
app.register_blueprint(blog_bp)


if __name__ == '__main__':
    manager.run()

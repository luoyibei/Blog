from flask import Blueprint
from flask import render_template,request,redirect,session
from user.models import User
from blog.models import Blog
from lib.orm import db
blog_bp = Blueprint('blog',__name__,url_prefix='/blog')
blog_bp.template_folder = './templates'



@blog_bp.route('/home')
def blog_home():
    blogs = Blog.query.all()
    name = request.args.get('username')
    # name = session.get('name')
    user = User.query.filter_by(username=name).one()
    # if user.username == session.get('name'):
    return render_template('blog_home.html',blogs = blogs,username =  name)

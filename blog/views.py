from flask import Blueprint
from flask import render_template,request,redirect,session
from user.models import User
from lib.orm import db
blog_bp = Blueprint('blog',__name__,url_prefix='/blog')
blog_bp.template_folder = './templates'


@blog_bp.route('/')
def home():
    return render_template('blog_home.html')

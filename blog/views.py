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
    # blog = Blog.query.filter_by(blogname=name).one()
    session['name'] = name
    # if user.username == session.get('name'):
    return render_template('blog_home.html',blogs = blogs,username =  name)

@blog_bp.route('/post',methods = ('POST','GET'))
def blog_post():
    if request.method == 'POST':
        blogname = request.form.get('blogname')
        blogcontent = request.form.get('blogcontent')
        blog = Blog(blogname=blogname,blogcontent=blogcontent)
        db.session.add(blog)
        db.session.commit()
        name = session.get('name')
        return redirect('/blog/read?id=%d'% blog.id)
    else:
        return render_template('blog_post.html')


@blog_bp.route('/read')
def blog_read():
    id = int(request.args.get('id'))
    blog = Blog.query.get(id)
    name = session.get('name')
    return render_template('blog_read.html',blog = blog,name = name)

@blog_bp.route('/delete')
def blog_delete():
    id = int(request.args.get('id'))
    Blog.query.filter_by(id = id).delete()
    db.session.commit()
    return redirect('/blog/home')

@blog_bp.route('/info')
def blog_info():
    return render_template('blog_info.html')


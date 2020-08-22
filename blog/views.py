from flask import Blueprint

blog_bp = Blueprint('blog',__name__,url_prefix='/blog')
blog_bp.template_folder = './templates'


@blog_bp.route('/')
def index():
    return 'blog'
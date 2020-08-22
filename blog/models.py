from lib.orm import db


class Blog(db.Model):
    __tablename__ = 'blog'

    id = db.Column(db.Integer, primary_key=True)
    blogname = db.Column(db.String(20),nullable=False)
    blogcontent = db.Column(db.Text)
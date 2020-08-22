from lib.orm import db


# User = {
#     'Tom' : {'name':'Tom','password':'123'},
#     'Jerry' : {'name':'Jerry','password':'223'}
# }

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20),unique=True)
    password = db.Column(db.String(128))
    city = db.Column(db.String(10))






#
# if __name__ == '__main__':
#     manager.run()




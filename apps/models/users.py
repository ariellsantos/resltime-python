from app import db

class User(db.Model):
    '''
    Modelo para usuarios
    '''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    apikey = db.Column(db.String(80), nullable=False)
    

    def __repr__(self):
        return "<Name: {}>".format(self.name)
from app import db

class Order(db.Model):
    """
    Modelo para ordenes 
    """
    id = db.Column(db.Integer, primary_key=True)
    nombre_cliente = db.Column(db.String(80), nullable=False)
    direccion_cliente = db.Column(db.String(80), nullable=False)
    telefono_cliente = db.Column(db.String(80), nullable=False)
    orden_cliente = db.Column(db.String(80), nullable=False)
    

    def __repr__(self):
        return "<id: {}>".format(self.id)
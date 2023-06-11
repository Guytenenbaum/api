from db import db

class Dish(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(200))
    price = db.Column(db.Integer)
    description = db.Column(db.Text)
    image = db.Column(db.Text)
    category = db.Column(db.Integer,db.ForeignKey('category.id'),nullable=False)

    def serialize(self):
        return {
            "id":self.id,
            "name":self.name,
            "price":self.price,
            "description":self.description,
            "image":self.image,
            "category":self.category.name
        }

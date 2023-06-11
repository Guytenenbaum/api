from db import db

class Category(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(200))
    image=db.Column(db.Text)

    def serialize(self):
        return {
            "id":self.id,
            "name":self.name,
            "image":self.image
        }


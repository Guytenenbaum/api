from flask import request
from flask_restful import Resource
from db import db
from models.category import Category
class CategoryAll(Resource):
    def get(self):
        categories = Category.query.all()
        return [category.serialize() for category in categories]

class CategoryOne(Resource):
    def get(self,id):
        category = Category.query.get(id)
        return category.serialize()

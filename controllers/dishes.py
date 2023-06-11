from flask import request
from flask_restful import Resource
from db import db
from models.dish import Dish

class DishFilter(Resource):
    def get(self,category_id):
        dishes = Dish.query.filter_by(category=category_id).all()
        return [dishes.serialize() for dish in dishes]
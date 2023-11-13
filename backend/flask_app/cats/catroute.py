
from flask import request
from flask_jwt_extended import jwt_required
from flask_restx import Resource, fields
from flask_jwt_extended import jwt_required
from flask_app.cats import ns
from flask_app.models import Cat

cat_model = ns.model(
    "cat",
    {
        "id": fields.Integer(),
        "image": fields.String(),
        "title": fields.String(),
        "description": fields.String(),
        "new_price": fields.Float(),
        "old_price": fields.Float(),
        "added_at": fields.DateTime(dt_format='iso8601')
        }
    )   
@ns.route('/cats')
class CatResource(Resource):
    @ns.expect(cat_model)
    @ns.marshal_list_with(cat_model)
    def get(self):
        """
            Get all cats in the list
        """
        cats = Cat.query.all()
        return cats
    
    @ns.marshal_with(cat_model)
    @ns.expect(cat_model)
    @jwt_required()
    def post(self):
        """Create new cat input"""
        cat = request.get_json()
        new_cat = Cat(
            image=cat.get('image'),
            title=cat.get('title'),
            description=cat.get('description'),
            new_price=cat.get('new_price'),
            old_price=cat.get('old_price')
            )
        new_cat.save()
        return new_cat



@ns.route('/cat/<int:id>')
class CatResource(Resource):
    @ns.marshal_with(cat_model)
    def get(self, id):
        """
        Get a recipe by id
        """
        cat = Cat.query.get_or_404(id)
        return cat
    @ns.marshal_with(cat_model)
    @jwt_required()     
    def put(self, id):
        cat_to_update = Cat.query.get_or_404(id)
        cat = request.get_json()
        cat_to_update.update(
            cat.get('image'),
            cat.get('title'),
            cat.get('description'),
            cat.get('new_price'),
            cat.get('old_price')
        )
        return cat_to_update
    
    @ns.marshal_with(cat_model)
    @jwt_required()
    def delete(self, id):
        cat_to_delete = Cat.query.get_or_404(id)
        cat_to_delete.delete()
        return cat_to_delete       

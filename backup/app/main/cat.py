from flask_restx import Resource, fields, Namespace
from flask_jwt_extended import jwt_required
from flask import request
from app.models.models import Cat
from app.main import bp

# Model serialization
cat_model = bp.model(
    "Cat",
    {
        "id": fields.Integer(),
        "image": fields.String(),
        "title": fields.String(),
        "description": fields.String(),
        "price_new": fields.Float(),
        "price_old": fields.Float()
    }
)


@bp.route('/cats')
class CatResource(Resource):
    @bp.marshal_list_with(cat_model)
    def get(self):
        """Get all cats in the database"""
        all_cats = Cat.query.all()
        return all_cats

    @bp.marshal_with(cat_model)
    @jwt_required()
    def post(self):
        """Create new cat input"""
        cat = request.get_json()
        new_cat = Cat(
            image=cat.get('image'),
            title=cat.get('title'),
            description=cat.get('description'),
            price_new=cat.get('price_new'),
            price_old=cat.get('price_old')
        )
        new_cat.save()
        return new_cat, 201


@bp.route('/cat/<int:id>')
class CatResource(Resource):
    @bp.marshal_with(cat_model)
    def get(self, id):
        """It gets cat by an id"""
        cat = Cat.query.get_or_404(id)
        return cat

    @bp.marshal_with(cat_model)
    @jwt_required()
    def put(self, id):
        """Update the cat entry by an id"""
        cat_to_update = Cat.query.get_or_404(id)
        data = request.get_json()
        cat_to_update.update(data.get('image'),
                             data.get('title'),
                             data.get('description'),
                             data.get('price_new'),
                             data.get('price_old')
                             )
        return cat_to_update

    @bp.marshal_with(cat_model)
    @jwt_required()
    def delete(self, id):
        """It deletes cat from the list using id"""
        cat_to_delete = Cat.query.get_or_404(id)
        cat_to_delete.delete()
        return cat_to_delete
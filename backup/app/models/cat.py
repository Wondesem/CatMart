from flask_restx import Resource, fields, Namespace
from flask_jwt_extended import jwt_required
from flask import request
from app.models.models import Cat

cat_ns = Namespace("cat", description="cat database lists")

# Model serialization
cat_model = cat_ns.model(
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


@cat_ns.route('/cats')
class CatResource(Resource):
    @cat_ns.marshal_list_with(cat_model)
    def get(self):
        """Get all cats in the database"""
        all_cats = Cat.query.all()
        return all_cats

    @cat_ns.marshal_with(cat_model)
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


@cat_ns.route('/cat/<int:id>')
class CatResource(Resource):
    @cat_ns.marshal_with(cat_model)
    def get(self, id):
        """It gets cat by an id"""
        cat = Cat.query.get_or_404(id)
        return cat

    @cat_ns.marshal_with(cat_model)
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

    @cat_ns.marshal_with(cat_model)
    @jwt_required()
    def delete(self, id):
        """It deletes cat from the list using id"""
        cat_to_delete = Cat.query.get_or_404(id)
        cat_to_delete.delete()
        return cat_to_delete
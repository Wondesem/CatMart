from flask_app.exts import db
from datetime import datetime
"""
    class Cat:
    id: integer
    image: string(path of the image)
    title: string
    description: str(text)
    new_price: float
    old_price: float
    added_at: time added in
"""
class Cat(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    image = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    new_price = db.Column(db.Float(), nullable=False)
    old_price = db.Column(db.Float(), nullable=False)
    added_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"<Cat {self.title}>"
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self, image, title, description, price_new, price_old):
        self.image = image
        self.title = title
        self.description = description
        self.price_new = price_new
        self.price_old = price_old
        db.session.commit()

# User model
"""
class User:
    id: integer
    username: string
    email: string
    password: string
"""
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.Text(), nullable=False)
    member_since = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"<User {self.username}>"

    def save(self):
        db.session.add(self)
        db.session.commit()
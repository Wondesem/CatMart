from app.exts import db


"""
class Cat:
    id: int primary key
    image: str
    title:str
    description:text
    price_new: float
    price_old: float

"""


class Cat(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    image = db.Column(db.String(120))
    title = db.Column(db.String(), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    price_new = db.Column(db.Float(), nullable=False)
    price_old = db.Column(db.Float())

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

    def __repr__(self):
        return f"<User {self.username}>"

    def save(self):
        db.session.add(self)
        db.session.commit()
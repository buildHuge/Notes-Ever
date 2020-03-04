from notes_ever import db

class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(256), nullable=False , index=True, unique=True)

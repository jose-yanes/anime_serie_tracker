from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///anime_serie.db"
db.init_app(app)
#Create table

class Anime(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    title_jpn: Mapped[str] = mapped_column(String(250), unique=True, nullable=True)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return "Test"


if __name__ == "__main__":
    app.run(debug=True)
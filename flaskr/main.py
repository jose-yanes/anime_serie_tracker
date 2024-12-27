from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
import requests

app = Flask(__name__)

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///anime_serie.db"
db.init_app(app)
#Create table

class Anime(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    ani_id: Mapped[int] = mapped_column(Integer, nullable=False)
    title: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    title_native: Mapped[str] = mapped_column(String(100), unique=True, nullable=True)
    title_romanji: Mapped[str] = mapped_column(String(100), unique=True, nullable=True)
    episodes: Mapped[int] = mapped_column(Integer)
    average_score: Mapped[int] = mapped_column(Integer)
    cover_image: Mapped[str] = mapped_column(String(200), unique=True, nullable=True)
    color: Mapped[str] = mapped_column(String(6), unique=False, nullable=True)

query = '''
query ($search: String!) {
  Page {
    media(search: $search, type: ANIME) {
      id
      title {
        romaji
        english
        native
      }
      episodes
      averageScore
      bannerImage
      coverImage {
        large
        color
      }
      
    }
  }
}
'''

variables={
    "search": "naruto"
}
url = 'https://graphql.anilist.co'

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    response = requests.post(url, json={"query":query, "variables": variables}).json()
    print(f"Response: {response}")
    return "Hola"


if __name__ == "__main__":
    app.run(debug=True)
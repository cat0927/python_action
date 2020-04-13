from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)

# 初始化对象
db = SQLAlchemy(app)
db.create_all()


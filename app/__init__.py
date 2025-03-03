from flask import Flask
from flask_mail import Mail
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

mail = Mail(app)  # Initialize mail

from app import views  # Import views after initializing app and mail

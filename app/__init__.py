from flask import Flask

app = Flask(__name__)

from app import view
from app import admin_view
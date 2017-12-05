from flask import Blueprint

mapis = Blueprint('mapis',__name__)

from . import views

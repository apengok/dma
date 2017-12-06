from flask import Blueprint

mapis = Blueprint('mapis',__name__,template_folder='templates/map')

from . import views

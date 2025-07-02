# типо index.js
from .settings import project
from .urls import *


project.register_blueprint(blueprint= home.home)
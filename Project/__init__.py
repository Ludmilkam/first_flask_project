# типо index.js
from .settings import project
from .urls import *
from .loadenv import execute


project.register_blueprint(blueprint= home.home)
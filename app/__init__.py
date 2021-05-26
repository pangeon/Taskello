from flask import Flask

app = Flask(
    __name__, 
    static_url_path='', 
    static_folder='web/static', 
    template_folder='web/templates'
)

from app import routes


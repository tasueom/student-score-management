from flask import Flask

app = Flask(__name__)

def create_app():
    from app import routes
    
    return app
from flask import Flask

app = Flask(__name__)

def create_app():
    app.config['SECRET_KEY'] = 'secret_key1234'
    
    from app import routes
    
    return app
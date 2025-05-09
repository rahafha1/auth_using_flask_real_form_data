from flask import Flask, render_template
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from config import Config
from models import db
from routes.auth_routes import auth_bp
from routes.protected_routes import protected_bp

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
jwt = JWTManager(app)
CORS(app)

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(protected_bp, url_prefix='/api')

@app.route('/')
def home():
    return render_template('form.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
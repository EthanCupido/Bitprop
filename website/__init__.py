from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os 
from flask_login import LoginManager
from flask_mail import Mail
db = SQLAlchemy()
mail = Mail()

basedir = os.path.abspath(os.path.dirname(__file__))



def create_app():
    app= Flask(__name__)
    
    
    app.config["SECRET_KEY"] = "bitprop"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///" + os.path.join(basedir, "bitprop.db")
    app.config["MAIL_SERVER"] = "sntp.gmail.com"
    app.config["MAIL_PORT"] = 25
    app.config["MAIL_USERNAME"] = "t6929406@gmail.com"
    app.config["MAIL_PASSWORD"] = "waei diqs oiep yixf"
    app.config["MAIL_USE_TLS"] = False
    app.config["MAIL_USE_SSL"] = True
    mail.init_app(app)
    db.init_app(app)

    
  


    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/") 
    app.register_blueprint(auth, url_prefix="/") 

    from .models import User, Note, Properties
    
    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))    


    
    return app




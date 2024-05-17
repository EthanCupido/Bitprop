from flask import Blueprint,render_template,request,flash
from flask_login import  login_required , current_user
from .models import Properties,Note,User
from . import db,mail
from flask_mail import Message
import smtplib
import json

views = Blueprint("views",__name__)


@views.route("/")

def home():
    return render_template("home.html", user=current_user)


@views.route("/public",methods = ["GET","POST"])
@login_required
def public():
    
    
    if request.method == "POST":
        id = request.form.get("prop_id")
        note = request.form.get("note")
        agents = User.query.filter_by(id=id).first()
        email = agents.email
        new_note = Note(data=note,user_id=current_user.id)
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login("t6929406@gmail.com","waei diqs oiep yixf")
        server.sendmail("t6929406@gmail.com",email, note)
        db.session.add(new_note)
        db.session.commit()
        flash("Request sent.",category="success")
        
        
    
    return render_template("public.html", user=current_user ,data=Properties.query.all() )

@views.route("/agents")
@login_required
def agents():
    data = Note.query.filter_by(id = current_user.id)
    return render_template("agents.html", user=current_user, data = data)
    

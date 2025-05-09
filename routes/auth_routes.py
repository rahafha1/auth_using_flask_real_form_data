
from flask import Blueprint, request, jsonify, redirect, url_for, render_template, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from models import db, User
import datetime

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')

    if not name or not email or not password:
        flash("All fields are required", 'error')
        return redirect(url_for('home'))

    if User.query.filter_by(email=email).first():
        flash("Email already registered", 'error')
        return redirect(url_for('home'))

    hashed_password = generate_password_hash(password)
    new_user = User(name=name, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    access_token = create_access_token(identity=new_user.id, expires_delta=datetime.timedelta(hours=1))

    return render_template('profile.html', user=new_user, token=access_token)

@auth_bp.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash("Invalid email or password", 'error')
        return redirect(url_for('home'))

    access_token = create_access_token(identity=user.id, expires_delta=datetime.timedelta(hours=1))

    return render_template('profile.html', user=user, token=None)  # No token shown

@auth_bp.route('/logout', methods=['POST'])
def logout():
    flash("Logged out successfully", 'success')
    return redirect(url_for('home'))

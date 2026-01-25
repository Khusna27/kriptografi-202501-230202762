from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = "edutoken_final_2026_key"

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'edutoken.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    history = db.relationship('ClaimHistory', backref='owner', lazy=True)

class ClaimHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    activity_name = db.Column(db.String(100))
    amount = db.Column(db.Integer)
    tx_hash = db.Column(db.String(100))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

with app.app_context():
    db.create_all()

@app.route("/")
def index():
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        session["user"] = username
        if not User.query.filter_by(username=username).first():
            db.session.add(User(username=username))
            db.session.commit()
        return redirect(url_for("dashboard"))
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if "user" not in session: return redirect(url_for("login"))
    return render_template("dashboard.html", user=session["user"])

@app.route("/materi")
def materi():
    if "user" not in session: return redirect(url_for("login"))
    return render_template("materi.html")

@app.route("/info_token")
def info_token():
    if "user" not in session: return redirect(url_for("login"))
    return render_template("info_token.html")

@app.route("/profil")
def profil():
    if "user" not in session: return redirect(url_for("login"))
    u = User.query.filter_by(username=session["user"]).first()
    h = ClaimHistory.query.filter_by(user_id=u.id).order_by(ClaimHistory.timestamp.desc()).all()
    return render_template("profil.html", user=session["user"], history=h)

@app.route("/record-claim", methods=["POST"])
def record_claim():
    data = request.get_json()
    u = User.query.filter_by(username=session["user"]).first()
    new_h = ClaimHistory(user_id=u.id, activity_name=data.get('activity'), amount=data.get('amount'), tx_hash=data.get('txHash'))
    db.session.add(new_h)
    db.session.commit()
    return jsonify({"status": "ok"})

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
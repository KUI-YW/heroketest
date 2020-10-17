# hello-login.py
from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager, login_user, login_required
from user import User

app = Flask(__name__)

# 追加
# セッションを使うためにシークレットキーが必要です
app.secret_key = 'secret key'

# flask-loginを設定
login_manager = LoginManager()
login_manager.init_app(app)

@app.route('/login', methods=['GET'])
def form():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    user = User()
    login_user(user)
    return redirect(url_for('dashboard'))

# 追加
# @login_requiredをつけることによって要ログインになります
@app.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
    return render_template('dashboard.html')

# 追加
# セッションからUserを引き当てるときのコールバックです
# ここではテストなのでUser()をそのまま渡していますが、
# return User.get(user_id) などでUserの引き当てを行うものです。
@login_manager.user_loader
def load_user(user_id):
        return User()

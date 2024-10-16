from flask import render_template, request, redirect, url_for
from flask_login import login_user,logout_user,current_user, login_required
from models import User

def register_routes(app,db,bcrypt):

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/signup', methods=['GET','POST'])
    def signup():
        if request.method == "GET":
            return render_template('signup.html')
        elif request.method == "POST":
            username = request.form['username']
            password = request.form['password']

            hashed_password = bcrypt.generate_password_hash(password)

            user = User(username=username, password=hashed_password)

            db.session.add(user)
            db.session.commit()
            return redirect(url_for('index'))

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        users = User.query.all()
        axrinci_user = users[1]
        sifre = axrinci_user.password
        print(sifre,'#&#^#^#&#^@&#^@^@&#^@^')
        if request.method == "GET":
            return render_template('login.html')
        elif request.method == "POST":
            username = request.form['username']
            password = request.form['password']

            user = User.query.filter_by(username=username).first()
            if bcrypt.check_password_hash(sifre,password):
                login_user(user)
                return redirect(url_for('index'))
            else:
                return 'Failed'


    @app.route('/logout')
    def logout():
        logout_user()
        return redirect(url_for('index'))

    @app.route('/secret')
    @login_required
    def secret():
        return  'No permission to access this page'

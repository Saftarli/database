from app import create_app,db

flask_app = create_app()

if __name__ == '__main__':
    with flask_app.app_context():
        db.create_all()
    flask_app.run(host='127.0.0.1',debug=True)
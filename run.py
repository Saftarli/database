from app import create_app,db
from dotenv import load_dotenv
import  os


load_dotenv()
x = os.getenv("FLASK_DEBUG")
esl_debug = x=='1'
flask_app = create_app()

if __name__ == '__main__':
    with flask_app.app_context():
        db.create_all()
    flask_app.run(host='127.0.0.1',debug=esl_debug)
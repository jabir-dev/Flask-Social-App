from flaskblog import create_app

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

# from run import app db = SQLAlchemy(app)

# db = create_engine('sqlite:///foo.db')

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask

# Do not confuse app the variable (which gets assigned the Flask instance)
# with app the package (from which we import the views module).
app = Flask(__name__)  # application object (of class Flask)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views, models

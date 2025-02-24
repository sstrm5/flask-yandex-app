from app import create_app
from app.extensions import db
import os


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.getenv('FLASK_PORT'))

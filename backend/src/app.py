from flask import Flask
from flask_cors import CORS
from routes.api import api

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Register API routes
app.register_blueprint(api, url_prefix='/api')

if __name__ == "__main__":
    app.run(debug=True)
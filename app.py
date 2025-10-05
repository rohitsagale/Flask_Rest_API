# app.py
from flask import Flask
from routes.notes_routes import notes_bp

app = Flask(__name__)
app.register_blueprint(notes_bp)

if __name__ == "__main__":
    app.run(debug=True)

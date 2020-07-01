from flask import Flask,jsonify
from flask_cors import CORS
import json, os, signal


app=Flask(__name__)

def create_app(config_filename):

    app.config.from_object(config_filename)

    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    from Model import db
    db.init_app(app)
    return app

@app.route('/stopServer', methods=['GET'])
def stopServer():
    os.kill(os.getpid(), signal.SIGINT)
    return jsonify({ "success": True, "message": "Server is shutting down..." })

if __name__ == "__main__":
    app = create_app("config")
    CORS(app)
    app.run(debug=True)

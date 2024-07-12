from flask import *
from file_handling import load_video

app = Flask(__name__)

@app.route("upload_video", methods=["POST"])
def upload_video():
    if "file" not in request.file:
        return jsonify({"error": "no file part"}), 400
    
    file = request.files["name"]
    
    if file.filename == "":
        return jsonify({"error": "no selected file"}), 400
    
    try:
        video = load_video(file)
    except AssertionError as e:
        return jsonify({"error": str(e)}), 400
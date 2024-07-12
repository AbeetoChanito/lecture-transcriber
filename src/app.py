from flask import *
from file_handling import load_video

app = Flask(__name__)

@app.route("/upload_video", methods=["POST"])
def upload_video():
    if "file" not in request.files:
        return jsonify({"error": "no file part"}), 400
    
    file = request.files["file"]
    
    if file.filename == "":
        return jsonify({"error": "no selected file"}), 400
    
    try:
        video_transcribed, audio_transcribed = load_video(file)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    return jsonify({
        "video_transcribed": video_transcribed,
        "audio_transcribed": audio_transcribed
    }), 200

@app.route("/")
def base():
    return send_from_directory("../client/build", "index.html")

@app.route("/<path:path>")
def home(path):
    if not path.endswith(".html"):
        path += ".html"
    
    return send_from_directory("../client/build", path)

if __name__ == "__main__":
    app.run(debug=True, port=3000)
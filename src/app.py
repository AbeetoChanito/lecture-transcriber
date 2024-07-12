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

if __name__ == "__main__":
    app.run(debug=True)
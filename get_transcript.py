from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/get_transcript/<video_id>', methods=['GET'])
def get_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_text = ' '.join([item['text'] for item in transcript])
        return jsonify({'transcript': transcript_text})
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run()

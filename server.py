"""
Flask web server for Emotion Detector application.
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def render_index_page():
    """
    Render the main index page.
    """
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Route that receives user input text and returns emotion analysis.
    """

    text_to_analyze = request.args.get("textToAnalyze")

    if text_to_analyze == "":
        return "Invalid text! Please try again."

    response = emotion_detector(text_to_analyze)

    if response is None:
        return "Invalid text! Please try again."

    anger = response["anger"]
    disgust = response["disgust"]
    fear = response["fear"]
    joy = response["joy"]
    sadness = response["sadness"]
    dominant = response["dominant_emotion"]

    result = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, "
        f"'fear': {fear}, 'joy': {joy}, 'sadness': {sadness}. "
        f"The dominant emotion is {dominant}."
    )

    return result

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

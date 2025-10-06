"""
Flask web server for the Emotion Detection application.
This app receives text input from the user and returns the detected emotion.
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detector import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    """
    Function written to display results from package.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    return f"""For the given statement, the system response is
    'anger': {anger}, 'disgust': {disgust}, 
    'fear': {fear}, 'joy': {joy}, and 'sadness': {sadness}. 
    The dominant emotion is <b>{dominant_emotion}</b>."""

@app.route("/")
def render_index_page():
    """
    To retrieve static html and display with results.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

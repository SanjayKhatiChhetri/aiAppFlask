"""
This module implements a Flask server for emotion detection.
It provides endpoints for detecting emotions in text and rendering the index page.
"""

import os
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Create the Flask app with the correct template and static folders
app = Flask("Emotion Detector",
            template_folder=os.path.join(current_dir, 'oaqjp-final-project-emb-ai', 'templates'),
            static_folder=os.path.join(current_dir, 'oaqjp-final-project-emb-ai', 'static'))

@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Endpoint for detecting emotions in text.
    
    Returns:
        str: A string containing the detected emotions or an error message.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    return (f"For the given statement, the system response is 'dominant emotion': "
            f"{response['dominant_emotion']}, with "
            f"anger: {response['anger']}, "
            f"disgust: {response['disgust']}, "
            f"fear: {response['fear']}, "
            f"joy: {response['joy']}, "
            f"sadness: {response['sadness']}")

@app.route("/")
def render_index_page():
    """
    Endpoint for rendering the index page.
    
    Returns:
        str: Rendered HTML content of the index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

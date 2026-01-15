'''
Code to deploy the Emotion Detector
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector')
def emot_detector():
    '''
    Function that gets text and returns the output of the emotion detector
    '''
    text = request.args.get('textToAnalyze')
    result = emotion_detector(text)
    dominant_emotion = result['dominant_emotion']
    if dominant_emotion is None:
        return 'Invalid text! Please try again!'
    del result['dominant_emotion']
    message = f'For the given statement, the system response is {str(result)[1:-1]}. \
    The dominant emotion is {dominant_emotion}.'
    return message

@app.route('/')
def render_index_page():
    '''
    Function to render the index.html file
    '''
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

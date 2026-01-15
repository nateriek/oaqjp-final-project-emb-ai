import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    my_obj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=my_obj, headers=headers)
    response_dict = json.loads(response.text)
    status = response.status_code
    print(status)
    if status == 400:
        emotions = {'anger': None, 'disgust': None, 'fear':None, 'joy':None, 'sadness':None, 'dominant_emotion':None}
    elif status == 200:
        emotions = response_dict['emotionPredictions'][0]['emotion']
        emotions['dominant_emotion'] = max(emotions, key=emotions.get)
    return emotions
import requests
import json

def emotion_detector(text_to_analyze):
    if not text_to_analyze.strip():
        return {
            'dominant_emotion': None,
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None
        }
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=header)
    
    if response.status_code == 400:
        return {
            'dominant_emotion': None,
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None
        }
    
    formatted_response = json.loads(response.text)
    emotion_predictions = formatted_response['emotionPredictions'][0]['emotion']
    
    dominant_emotion = max(emotion_predictions, key=emotion_predictions.get)
    
    result = {
        'dominant_emotion': dominant_emotion,
        'anger': emotion_predictions.get('anger'),
        'disgust': emotion_predictions.get('disgust'),
        'fear': emotion_predictions.get('fear'),
        'joy': emotion_predictions.get('joy'),
        'sadness': emotion_predictions.get('sadness')
    }
    
    return result
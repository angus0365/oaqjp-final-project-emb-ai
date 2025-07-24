import requests  # Import the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyse):  # Define a function named emotion_detector that takes a string input (text_to_analyse)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' # URL of the emotion analysis service
    myobj = { "raw_document": { "text": text_to_analyse } } # Create a dictionary with the text to be analyzed 
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} # Set the headers required for the API request
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    
    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    # Access the prediction
    prediction = formatted_response['emotionPredictions'][0]

    # Access the emotion dictionary inside the prediction
    emotion_scores = prediction['emotion']

    # Extract individual emotion scores
    anger_score = emotion_scores['anger']
    disgust_score = emotion_scores['disgust']
    fear_score = emotion_scores['fear']
    joy_score = emotion_scores['joy']
    sadness_score = emotion_scores['sadness']

    # Determine the dominant emotion
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    # Returning a dictionary containing emotion analysis results
    return {'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion}

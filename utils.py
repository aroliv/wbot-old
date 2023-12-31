import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "wbot-j9xk-c2ac56a1b0c0.json"

from google.cloud import dialogflow_v2 as dialogflow
dialogflow_session_client = dialogflow.SessionsClient()
PROJECT_ID = "wbot-j9xk"

def detect_intent_from_text(text, session_id, language_code='pt-br'):
    session = dialogflow_session_client.session_path(PROJECT_ID, session_id)
    text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)
    response = dialogflow_session_client.detect_intent(session=session, query_input=query_input)
    return response

def extract_media_url(response):
    # Extraia a URL da mídia da resposta do Dialogflow
    if response.query_result.webhook_payload and "media-url" in response.query_result.webhook_payload:
        return response.query_result.webhook_payload["media-url"]
    return None

def fetch_reply(query, session_id):
    response = detect_intent_from_text(query, session_id)
    fulfillment_text = response.query_result.fulfillment_text
    media_url = extract_media_url(response)

    return fulfillment_text, media_url
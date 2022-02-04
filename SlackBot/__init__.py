import logging
import os
from urllib import response
from slack import WebClient
from slack.errors import SlackApiError

import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    msg = req.params.get('msg')
    
    client = WebClient(token=os.environ['SLACK_API_TOKEN'])

    try:
        response = client.chat_postMessage(
            channel='#random',
            text=msg)
        assert response["message"]["text"] == msg
    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        assert e.response["ok"] is False
        assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
        logging.CRITICAL(f"Got an error: {e.response['error']}")
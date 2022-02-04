import logging
import os
from urllib import response
from slack import WebClient
from slack.errors import SlackApiError

import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    return func.HttpResponse(F"Hello! You're calling something that doesn't actually do anything yet. Come back later to see if anything interesting has happened.")

    # client = WebClient(token=os.environ['SLACK_API_TOKEN'])

    # try:
    #     response = client.chat_postMessage(
    #         channel='#random',
    #         text="Hello world!")
    #     assert response["message"]["text"] == "Hello world!"
    # except SlackApiError as e:
    #     # You will get a SlackApiError if "ok" is False
    #     assert e.response["ok"] is False
    #     assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
    #     print(f"Got an error: {e.response['error']}")
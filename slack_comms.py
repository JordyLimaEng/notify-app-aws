from slack_sdk import WebClient
from slack_sdk.webhook import WebhookClient
from slack_sdk.errors import SlackApiError
import logging
import properties as props

logging.basicConfig(level=logging.DEBUG)
webhook  = WebhookClient(props.SLACK_API_TOKEN)

def send_msg(text):
    try:
        response = webhook.send(
            text="Resultado da execução: ",
            attachments=[text]
        )
    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        assert e.response["error"]    # str like 'invalid_auth', 'channel_not_found'
    return response